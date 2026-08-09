const enhanceForm =
    document.getElementById("enhance-form");

const enhanceButton =
    document.getElementById("enhance-button");

const enhanceStatus =
    document.getElementById("enhance-status");

const resultsSection =
    document.getElementById("results-section");

const enhancedBulletsList =
    document.getElementById("enhanced-bullets");

const enhancementId =
    document.getElementById("enhancement-id");

const historyStatus =
    document.getElementById("history-status");

const historyList =
    document.getElementById("history-list");

const refreshHistoryButton =
    document.getElementById("refresh-history");


function setStatus(
    element,
    message,
    type = ""
) {

    element.textContent = message;

    element.className = "status";

    if (type) {
        element.classList.add(type);
    }
}


function getResumeBullets() {

    return document
        .getElementById("resume-bullets")
        .value
        .split("\n")
        .map(
            bullet => bullet.trim()
        )
        .filter(
            bullet => bullet.length > 0
        );
}


function displayEnhancedBullets(data) {

    enhancedBulletsList.innerHTML = "";

    data.enhancedBullets.forEach(
        bullet => {

            const listItem =
                document.createElement("li");

            listItem.textContent = bullet;

            enhancedBulletsList.appendChild(
                listItem
            );
        }
    );

    enhancementId.textContent =
        `Enhancement ID: ${data.enhancementId}`;

    resultsSection.classList.remove(
        "hidden"
    );
}


async function enhanceResume(event) {

    event.preventDefault();

    const jobDescription =
        document
            .getElementById("job-description")
            .value
            .trim();

    const resumeBullets =
        getResumeBullets();

    if (!jobDescription) {

        setStatus(
            enhanceStatus,
            "Please enter a job description.",
            "error"
        );

        return;
    }

    if (resumeBullets.length === 0) {

        setStatus(
            enhanceStatus,
            "Please enter at least one resume bullet.",
            "error"
        );

        return;
    }

    enhanceButton.disabled = true;

    setStatus(
        enhanceStatus,
        "Enhancing resume..."
    );

    try {

        const response =
            await fetch(
                `${CONFIG.API_BASE_URL}${CONFIG.ENDPOINTS.ENHANCE}`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        jobDescription,
                        resumeBullets
                    })
                }
            );

        const data =
            await response.json();

        if (!response.ok) {

            throw new Error(
                data.error ||
                "Unable to enhance resume."
            );
        }

        displayEnhancedBullets(data);

        setStatus(
            enhanceStatus,
            "Resume enhanced successfully.",
            "success"
        );

        await loadHistory();

    }
    catch (error) {

        setStatus(
            enhanceStatus,
            error.message,
            "error"
        );

    }
    finally {

        enhanceButton.disabled = false;
    }
}


function displayHistory(history) {

    historyList.innerHTML = "";

    if (history.length === 0) {

        historyList.textContent =
            "No enhancement history available.";

        return;
    }

    history.forEach(item => {

        const container =
            document.createElement("div");

        container.className =
            "history-item";

        const createdAt =
            document.createElement("p");

        createdAt.className =
            "metadata";

        createdAt.textContent =
            `Created: ${
                item.createdAt.split("#")[0]
            }`;

        const list =
            document.createElement("ul");

        item.enhancedBullets.forEach(
            bullet => {

                const listItem =
                    document.createElement("li");

                listItem.textContent = bullet;

                list.appendChild(
                    listItem
                );
            }
        );

        container.appendChild(createdAt);

        container.appendChild(list);

        historyList.appendChild(container);

    });

}


async function loadHistory() {

    setStatus(
        historyStatus,
        "Loading enhancement history..."
    );

    try {

        const response =
            await fetch(
                `${CONFIG.API_BASE_URL}${CONFIG.ENDPOINTS.HISTORY}`
            );

        const data =
            await response.json();

        if (!response.ok) {

            throw new Error(
                data.error ||
                "Unable to retrieve history."
            );
        }

        displayHistory(
            data.history
        );

        setStatus(
            historyStatus,
            ""
        );

    }
    catch (error) {

        setStatus(
            historyStatus,
            error.message,
            "error"
        );
    }

}


enhanceForm.addEventListener(
    "submit",
    enhanceResume
);

refreshHistoryButton.addEventListener(
    "click",
    loadHistory
);

document.title = CONFIG.APP_NAME;

loadHistory();