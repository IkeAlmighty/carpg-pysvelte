# CARPG

## Development Setup
1. Open terminal and run
    ```
    python -m venv venv
    ./venv/Scripts/activate
    pip install -r requirements.txt
    ```
    This creates a python virtual environment and installs backend dependencies.

2. For the frontend, install node and npm, and then run:
    ```
    cd svelte-client
    npm install
    ```

3. To start the backend in development mode, open terminal and run the dev.* file that matches your OS. (Macs and Linux run dev.sh, Windows can run dev.ps1)

4. To start the frontend in development mode, open a new terminal and run
    ```
    cd svelte-client
    npm run dev
    ```

http://localhost:5001 should show the svelte-client app.