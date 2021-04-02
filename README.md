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

5. As an alternative to 3 and 4, simply run ./dev_all.sh to start both servers (backend as a background process). Not super good for finding error messages though.

http://localhost:5001 should show the svelte-client app.

http://localhost:5000 should show the flask app.

## Creating Simple API Endpoints
Although it probably won't last the way it is, 
currently a new api endpoint can be added by
creating a new module in the api package and 
adding:
```python
def get():
    return 'example response'
```
This will map the filename to an endpoint of
/api/\<filename\>