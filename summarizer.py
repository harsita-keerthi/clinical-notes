from transformers import pipeline

# load summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    # perform summarization
    summary = summarizer(text, max_length=200, min_length=40, do_sample=False)
    return summary[0]['summary_text']
