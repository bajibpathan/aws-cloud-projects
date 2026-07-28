"use strict";

// ====================================================
// AWS AND APPLICATION CONFIGURATION
// ====================================================

const AWS_REGION = "us-east-1";

// Hardcode your actual Cognito User Pool ID.
const USER_POOL_ID =
    "us-east-1_TsCCSPWHk";

// Hardcode your Cognito App Client ID.
// The app client must not have a client secret.
const APP_CLIENT_ID =
    "1u04rpjstnd2gfln2gjk4g36a9";

// HTTP API invoke URL.
//
// For a $default stage:
// https://abc123.execute-api.us-east-1.amazonaws.com
//
// For a named stage such as prod:
// https://abc123.execute-api.us-east-1.amazonaws.com/prod
const HTTP_API_BASE_URL =
    "https://hb0ax3zisl.execute-api.us-east-1.amazonaws.com";

// Change this to match your HTTP API route.
const UPLOAD_ROUTE = "/upload-url";

// HTTP API JWT authorizer will use the Cognito access token.
const API_TOKEN_STORAGE_KEY = "accessToken";

// Resume upload restrictions.
const ALLOWED_FILE_TYPE = "application/pdf";
const MAX_FILE_SIZE_BYTES = 5 * 1024 * 1024;

// ====================================================
// HTML ELEMENTS
// ====================================================

const loginForm =
    document.getElementById("login-form");

const loginSection =
    document.getElementById("login-section");

const uploadSection =
    document.getElementById("upload-section");

const emailInput =
    document.getElementById("email");

const passwordInput =
    document.getElementById("password");

const resumeFileInput =
    document.getElementById("resume-file");

const signedInUser =
    document.getElementById("signed-in-user");

const statusMessage =
    document.getElementById("status-message");

const signInButton =
    document.getElementById("sign-in-button");

const uploadButton =
    document.getElementById("upload-button");

const signOutButton =
    document.getElementById("sign-out-button");

// ====================================================
// AMAZON COGNITO CONFIGURATION
// ====================================================

const poolData = {
    UserPoolId: USER_POOL_ID,
    ClientId: APP_CLIENT_ID
};

const userPool =
    new AmazonCognitoIdentity.CognitoUserPool(poolData);

// ====================================================
// EVENT LISTENERS
// ====================================================

loginForm.addEventListener(
    "submit",
    handleLogin
);

uploadButton.addEventListener(
    "click",
    uploadResume
);

signOutButton.addEventListener(
    "click",
    signOut
);

// ====================================================
// LOGIN HANDLING
// ====================================================

function handleLogin(event) {
    event.preventDefault();

    const username = emailInput.value.trim();
    const password = passwordInput.value;

    if (!username || !password) {
        setStatus(
            "Enter your email or username and password.",
            "error"
        );

        return;
    }

    signIn(username, password);
}

function signIn(username, password) {
    setLoginLoading(true);

    setStatus(
        "Signing in to Amazon Cognito..."
    );

    const authenticationDetails =
        new AmazonCognitoIdentity.AuthenticationDetails({
            Username: username,
            Password: password
        });

    const cognitoUser =
        new AmazonCognitoIdentity.CognitoUser({
            Username: username,
            Pool: userPool
        });

    cognitoUser.authenticateUser(
        authenticationDetails,
        {
            onSuccess: function (session) {
                saveSession(
                    session,
                    username
                );

                passwordInput.value = "";

                showAuthenticatedView(
                    username
                );

                setStatus(
                    "Signed in successfully.",
                    "success"
                );

                setLoginLoading(false);
            },

            onFailure: function (error) {
                console.error(
                    "Cognito sign-in error:",
                    error
                );

                handleAuthenticationError(
                    error
                );

                setLoginLoading(false);
            },

            newPasswordRequired: function () {
                setStatus(
                    "A new password is required for this account. Set a permanent password before continuing.",
                    "error"
                );

                setLoginLoading(false);
            },

            mfaRequired: function () {
                setStatus(
                    "MFA is required, but MFA support has not yet been added to this web client.",
                    "error"
                );

                setLoginLoading(false);
            },

            totpRequired: function () {
                setStatus(
                    "Authenticator verification is required, but it has not yet been added to this web client.",
                    "error"
                );

                setLoginLoading(false);
            }
        }
    );
}

// ====================================================
// SAVE COGNITO SESSION
// ====================================================

function saveSession(session, username) {
    const idToken =
        session.getIdToken().getJwtToken();

    const accessToken =
        session.getAccessToken().getJwtToken();

    const refreshToken =
        session.getRefreshToken().getToken();

    sessionStorage.setItem(
        "idToken",
        idToken
    );

    sessionStorage.setItem(
        "accessToken",
        accessToken
    );

    sessionStorage.setItem(
        "refreshToken",
        refreshToken
    );

    sessionStorage.setItem(
        "username",
        username
    );
}

// ====================================================
// AUTHENTICATION ERROR HANDLING
// ====================================================

function handleAuthenticationError(error) {
    const errorName =
        error?.name ||
        error?.code ||
        "UnknownError";

    switch (errorName) {
        case "NotAuthorizedException":
            setStatus(
                "Incorrect username or password.",
                "error"
            );
            break;

        case "UserNotFoundException":
            setStatus(
                "Incorrect username or password.",
                "error"
            );
            break;

        case "UserNotConfirmedException":
            setStatus(
                "This Cognito user has not been confirmed.",
                "error"
            );
            break;

        case "PasswordResetRequiredException":
            setStatus(
                "A password reset is required for this account.",
                "error"
            );
            break;

        case "TooManyRequestsException":
            setStatus(
                "Too many sign-in attempts. Try again later.",
                "error"
            );
            break;

        case "LimitExceededException":
            setStatus(
                "The Cognito request limit was exceeded. Try again later.",
                "error"
            );
            break;

        case "NetworkError":
            setStatus(
                "Unable to connect to Amazon Cognito. Check your internet connection.",
                "error"
            );
            break;

        default:
            setStatus(
                "Unable to sign in. Check the browser console for details.",
                "error"
            );
    }
}

// ====================================================
// RESUME UPLOAD
// ====================================================

async function uploadResume() {
    const file =
        resumeFileInput.files[0];

    const validationError =
        validateResumeFile(file);

    if (validationError) {
        setStatus(
            validationError,
            "error"
        );

        return;
    }

    const accessToken =
        sessionStorage.getItem(
            API_TOKEN_STORAGE_KEY
        );

    if (!accessToken) {
        handleInvalidSession(
            "Your session is unavailable. Sign in again."
        );

        return;
    }

    if (isTokenExpired(accessToken)) {
        handleInvalidSession(
            "Your access token expired. Sign in again."
        );

        return;
    }

    try {
        setUploadLoading(true);

        setStatus(
            "Requesting a secure upload URL..."
        );

        const uploadData =
            await requestUploadUrl(
                file,
                accessToken
            );

        console.log(
            "Upload metadata:",
            {
                uploadId: uploadData.uploadId,
                objectKey: uploadData.objectKey,
                expiresIn: uploadData.expiresIn
            }
        );

        const uploadUrl =
            getUploadUrlFromResponse(
                uploadData
            );

        setStatus(
            "Uploading resume directly to Amazon S3..."
        );

        await uploadFileToS3(
            file,
            uploadUrl
        );

        resumeFileInput.value = "";

        setStatus(
            "Resume uploaded successfully. Backend processing has started.",
            "success"
        );
    } catch (error) {
        console.error(
            "Resume upload failed:",
            error
        );

        setStatus(
            error.message ||
                "Resume upload failed.",
            "error"
        );
    } finally {
        setUploadLoading(false);
    }
}

// ====================================================
// FILE VALIDATION
// ====================================================

function validateResumeFile(file) {
    if (!file) {
        return "Select a PDF resume before uploading.";
    }

    const fileName =
        file.name.toLowerCase();

    const hasPdfExtension =
        fileName.endsWith(".pdf");

    if (
        file.type !== ALLOWED_FILE_TYPE ||
        !hasPdfExtension
    ) {
        return "Only PDF resumes are supported.";
    }

    if (file.size === 0) {
        return "The selected PDF is empty.";
    }

    if (file.size > MAX_FILE_SIZE_BYTES) {
        return "The PDF must be 5 MB or smaller.";
    }

    return null;
}

// ====================================================
// CALL API GATEWAY HTTP API
// ====================================================

async function requestUploadUrl(
    file,
    accessToken
) {
    const endpoint =
        buildApiUrl(
            HTTP_API_BASE_URL,
            UPLOAD_ROUTE
        );

    console.log(
        "Calling HTTP API route:",
        endpoint
    );

    const response = await fetch(
        endpoint,
        {
            method: "POST",

            headers: {
                Authorization:
                    `Bearer ${accessToken}`,

                "Content-Type":
                    "application/json"
            },

            body: JSON.stringify({
                filename: file.name,
                contentType: file.type,
                fileSize: file.size
            })
        }
    );

    if (
        response.status === 401 ||
        response.status === 403
    ) {
        clearSession();
        showSignedOutView();

        throw new Error(
            "The HTTP API rejected the access token. Sign in again or verify the JWT authorizer configuration."
        );
    }

    if (!response.ok) {
        const errorBody =
            await readResponseSafely(
                response
            );

        console.error(
            "HTTP API error:",
            {
                status: response.status,
                statusText:
                    response.statusText,
                responseBody:
                    errorBody
            }
        );

        throw new Error(
            `Unable to create the upload URL. HTTP API returned ${response.status}.`
        );
    }

    let data;

    try {
        data = await response.json();
    } catch (error) {
        console.error(
            "Unable to parse HTTP API response:",
            error
        );

        throw new Error(
            "The HTTP API returned an invalid JSON response."
        );
    }

    console.log(
        "HTTP API request completed successfully."
    );

    return data;
}

// ====================================================
// HANDLE DIFFERENT LAMBDA RESPONSE PROPERTY NAMES
// ====================================================

function getUploadUrlFromResponse(data) {
    const uploadUrl =
        data.uploadUrl ||
        data.presignedUrl ||
        data.presigned_url;

    if (!uploadUrl) {
        console.error(
            "Unexpected HTTP API response:",
            data
        );

        throw new Error(
            "The HTTP API response did not contain an upload URL."
        );
    }

    return uploadUrl;
}

// ====================================================
// UPLOAD FILE DIRECTLY TO S3
// ====================================================

async function uploadFileToS3(
    file,
    uploadUrl
) {
    const response = await fetch(
        uploadUrl,
        {
            method: "PUT",

            headers: {
                "Content-Type":
                    file.type
            },

            body: file
        }
    );

    if (!response.ok) {
        const errorBody =
            await readResponseSafely(
                response
            );

        console.error(
            "Amazon S3 upload error:",
            {
                status: response.status,
                statusText:
                    response.statusText,
                responseBody:
                    errorBody
            }
        );

        throw new Error(
            `Amazon S3 upload failed with status ${response.status}.`
        );
    }
}

// ====================================================
// SIGN OUT
// ====================================================

function signOut() {
    const cognitoUser =
        userPool.getCurrentUser();

    if (cognitoUser) {
        cognitoUser.signOut();
    }

    clearSession();
    showSignedOutView();

    setStatus(
        "You have signed out successfully."
    );
}

// ====================================================
// RESTORE EXISTING SESSION
// ====================================================

function restoreSession() {
    const accessToken =
        sessionStorage.getItem(
            API_TOKEN_STORAGE_KEY
        );

    const username =
        sessionStorage.getItem(
            "username"
        );

    if (!accessToken || !username) {
        clearSession();
        showSignedOutView();

        return;
    }

    if (isTokenExpired(accessToken)) {
        clearSession();
        showSignedOutView();

        setStatus(
            "Your previous session expired. Sign in again."
        );

        return;
    }

    showAuthenticatedView(
        username
    );

    setStatus(
        "Existing browser session restored.",
        "success"
    );
}

// ====================================================
// JWT EXPIRATION CHECK
// ====================================================

function isTokenExpired(token) {
    try {
        const payload =
            decodeJwtPayload(token);

        if (!payload.exp) {
            return true;
        }

        return (
            Date.now() >=
            payload.exp * 1000
        );
    } catch (error) {
        console.error(
            "Unable to decode JWT:",
            error
        );

        return true;
    }
}

function decodeJwtPayload(token) {
    const tokenParts =
        token.split(".");

    if (tokenParts.length !== 3) {
        throw new Error(
            "Invalid JWT structure."
        );
    }

    const payloadPart =
        tokenParts[1]
            .replace(/-/g, "+")
            .replace(/_/g, "/");

    const paddedPayload =
        payloadPart.padEnd(
            payloadPart.length +
                (
                    4 -
                    payloadPart.length % 4
                ) % 4,
            "="
        );

    const decodedPayload =
        atob(paddedPayload);

    const jsonPayload =
        decodeURIComponent(
            decodedPayload
                .split("")
                .map(function (character) {
                    return (
                        "%" +
                        character
                            .charCodeAt(0)
                            .toString(16)
                            .padStart(2, "0")
                    );
                })
                .join("")
        );

    return JSON.parse(
        jsonPayload
    );
}

// ====================================================
// SESSION HELPERS
// ====================================================

function handleInvalidSession(message) {
    clearSession();
    showSignedOutView();

    setStatus(
        message,
        "error"
    );
}

function clearSession() {
    sessionStorage.removeItem(
        "idToken"
    );

    sessionStorage.removeItem(
        "accessToken"
    );

    sessionStorage.removeItem(
        "refreshToken"
    );

    sessionStorage.removeItem(
        "username"
    );
}

// ====================================================
// PAGE DISPLAY HELPERS
// ====================================================

function showAuthenticatedView(username) {
    loginSection.hidden = true;
    uploadSection.hidden = false;

    signedInUser.textContent =
        `Signed in as: ${username}`;
}

function showSignedOutView() {
    loginSection.hidden = false;
    uploadSection.hidden = true;

    signedInUser.textContent = "";

    passwordInput.value = "";
    resumeFileInput.value = "";
}

function setLoginLoading(isLoading) {
    signInButton.disabled =
        isLoading;

    signInButton.textContent =
        isLoading
            ? "Signing In..."
            : "Sign In";
}

function setUploadLoading(isLoading) {
    uploadButton.disabled =
        isLoading;

    signOutButton.disabled =
        isLoading;

    uploadButton.textContent =
        isLoading
            ? "Uploading..."
            : "Upload Resume";
}

function setStatus(
    message,
    type = "normal"
) {
    statusMessage.textContent =
        message;

    statusMessage.classList.remove(
        "error-message",
        "success-message"
    );

    if (type === "error") {
        statusMessage.classList.add(
            "error-message"
        );
    }

    if (type === "success") {
        statusMessage.classList.add(
            "success-message"
        );
    }
}

// ====================================================
// URL AND RESPONSE HELPERS
// ====================================================

function buildApiUrl(
    baseUrl,
    route
) {
    const normalizedBaseUrl =
        baseUrl.endsWith("/")
            ? baseUrl.slice(0, -1)
            : baseUrl;

    const normalizedRoute =
        route.startsWith("/")
            ? route
            : `/${route}`;

    return (
        normalizedBaseUrl +
        normalizedRoute
    );
}

async function readResponseSafely(
    response
) {
    try {
        return await response.text();
    } catch {
        return "Unable to read response body.";
    }
}

// ====================================================
// PAGE INITIALIZATION
// ====================================================

restoreSession();