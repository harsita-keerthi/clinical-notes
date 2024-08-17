from transformers import pipeline

# load summarization pipeline
summarizer = pipeline("summarization")

def summarize_text(text):
    # perform summarization
    summary = summarizer(
        text,
        max_length=500,  
        min_length=100,  
        do_sample=False,
        truncation=True  
    )
    return summary[0]['summary_text']
