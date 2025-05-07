import streamlit as st


def main():
    st.title("BTCAUDash")

    with open("plots/toggle_lines.html", "r") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=600, width=900)


if __name__ == "__main__":
    main()
