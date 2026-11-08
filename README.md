# SeeLess — Iteration 1 MVP

SeeLess adds spoken descriptions of on-screen actions to video, timed to fit in natural pauses between dialogue. The frontend explains the workflow and includes a demo MP4 picker. Video analysis and generation services are not connected in this MVP scaffold.

## Run with Streamlit

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Deploy on GitHub Pages

The static frontend is `index.html` at the repository root. In GitHub, open **Settings → Pages**, choose **Deploy from a branch**, then select the `main` branch and `/ (root)`. GitHub Pages will publish the site after the workflow completes.

## Deploy on Streamlit Community Cloud

Push this repository to GitHub, then create an app in Streamlit Community Cloud with the repository, branch `main`, and main file path `app.py`. Community Cloud installs `requirements.txt` automatically.
