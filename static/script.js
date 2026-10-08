async function askQuestion() {

    const questionInput =
        document.getElementById("question");

    const answerDiv =
        document.getElementById("answer");

    const question =
        questionInput.value.trim();


    if (!question) {

        answerDiv.textContent =
            "Please enter a question.";

        return;
    }


    answerDiv.textContent =
        "Thinking...";


    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });


        const data = await response.json();


        if (!response.ok) {

            answerDiv.textContent =
                data.detail || "Something went wrong.";

            return;
        }


        // Display answer

        answerDiv.textContent =
            data.answer;


        // Display sources

        displaySources(
            data.sources,
            data.distances
        );


    } catch (error) {

        answerDiv.textContent =
            "Could not connect to the server.";

        console.error(error);
    }
}


function displaySources(
    sources,
    distances
) {

    const sourcesDiv =
        document.getElementById("sources");


    sourcesDiv.innerHTML = "";


    sources.forEach(
        (source, index) => {

            const sourceItem =
                document.createElement("div");

            sourceItem.className =
                "source-item";


            sourceItem.innerHTML = `
                <strong>
                    ${index + 1}. ${source.source}
                </strong>

                <br>

                Chunk:
                ${source.chunk}

                <br>

                Distance:
                ${distances[index]}
            `;


            sourcesDiv.appendChild(
                sourceItem
            );

        }
    );
}