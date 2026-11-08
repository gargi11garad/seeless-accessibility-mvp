import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="SeeLess — Stories, fully heard.",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep the Streamlit chrome out of the way so the same responsive frontend
# can be presented here and on GitHub Pages.
st.markdown(
    """
    <style>
      #MainMenu, footer, header { visibility: hidden; }
      [data-testid="stAppViewContainer"] { background: #090e18; }
      [data-testid="stMainBlockContainer"] { padding: 0; max-width: 100%; }
      iframe { border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

page = Path(__file__).parent / "outputs" / "index.html"
if not page.exists():
    page = Path(__file__).parent / "index.html"

components.html(page.read_text(encoding="utf-8"), height=2900, scrolling=True)
