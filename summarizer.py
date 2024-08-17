# summarizer.py - 
# This file contains the NLP model to summarize clinical notes. 
# It is imported to app.py for integration with frontend


from transformers import pipeline   # import transformer from Hugging Face for NLP pipeline

# load summarization pipeline from import 
summarizer = pipeline("summarization")

def summarize_text(text):
    # perform summarization 
    # tune parameters to improve model performance
    summary = summarizer(
        text,   # txt files
        max_length=500,     # max length of generated summary
        min_length=100,     # min length of generated summary
        do_sample=False,    
        truncation=True     # if file size is too large, turncate values
    )
    return summary[0]['summary_text']
