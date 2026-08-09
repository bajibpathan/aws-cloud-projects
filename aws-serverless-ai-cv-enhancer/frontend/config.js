/**
 * ============================================================================
 * Serverless AI CV Enhancer
 * Frontend Configuration
 * ============================================================================
 *
 * This file contains environment-specific configuration for the frontend.
 * Keeping configuration separate from application logic makes it easier
 * to maintain and deploy the application across different environments.
 *
 * Update API_BASE_URL when the API Gateway endpoint changes.
 * ============================================================================
 */

const CONFIG = {

    // -------------------------------------------------------------------------
    // Application
    // -------------------------------------------------------------------------

    APP_NAME: "Serverless AI CV Enhancer",

    APP_VERSION: "1.0.0",

    // -------------------------------------------------------------------------
    // API Gateway
    // -------------------------------------------------------------------------

    API_BASE_URL:
        "https://YOUR_API_ID.execute-api.ca-central-1.amazonaws.com",

    ENDPOINTS: {

        ENHANCE: "/enhance",

        HISTORY: "/history"

    },

    // -------------------------------------------------------------------------
    // Network
    // -------------------------------------------------------------------------

    REQUEST_TIMEOUT: 30000

};