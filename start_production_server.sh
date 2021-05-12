cd flask-backend && gunicorn app:server &
cd svelte-client && npm run build && npm run start &