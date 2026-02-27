import gradio as gr
from pathlib import Path

from rag_app import ask

APP_TITLE = "Sumeru Incident RAG Assistant (Local CPU)"
APP_DESC = """
Paste an incident ticket / timeline / notes.  
The assistant retrieves similar historical incidents from the KB (Chroma) and generates:
- missing info checklist
- clarifying questions
- likely next steps
- citations to incident documents
"""

DEFAULT_TEXT = """We are seeing login failures in production after a config change.
Users get 401 Unauthorized on /oauth/token. Possible token validation issue.
Please list missing info, clarifying questions, and suggest next actions.
"""

def format_sources(docs):
    lines = []
    for i, d in enumerate(docs, start=1):
        src = d.metadata.get("source", "unknown")
        # Make it short in UI
        src_short = str(src).replace("data/kb_md/", "")
        lines.append(f"[{i}] {src_short}")
    return "\n".join(lines)

def run_rag(user_input, top_k):
    if not user_input or not user_input.strip():
        return "Please paste an incident description.", ""

    answer, docs = ask(user_input, k=int(top_k))
    sources = format_sources(docs)
    return answer, sources

with gr.Blocks(title=APP_TITLE) as demo:
    gr.Markdown(f"# {APP_TITLE}")
    gr.Markdown(APP_DESC)

    with gr.Row():
        top_k = gr.Slider(minimum=3, maximum=10, value=6, step=1, label="Top-K retrieved incidents")

    inp = gr.Textbox(
        label="Incident Input (ticket/timeline/log snippet)",
        lines=10,
        value=DEFAULT_TEXT
    )

    btn = gr.Button("Analyze Incident")

    out_answer = gr.Textbox(label="RAG Assistant Output", lines=18)
    out_sources = gr.Textbox(label="Retrieved Sources (Evidence)", lines=8)

    btn.click(run_rag, inputs=[inp, top_k], outputs=[out_answer, out_sources])

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, show_api=False)