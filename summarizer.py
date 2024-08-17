

from transformers import pipeline

# Attempt to load the summarization pipeline
try:
    summarizer = pipeline("summarization")
except Exception as e:
    raise RuntimeError(f"Failed to load the summarization model: {e}")

def summarize_text(text):
    try:
        if not isinstance(text, str):
            raise ValueError("Input text must be a string.")
        
        # perform summarization
        summary = summarizer(
            text,  # txt files
            max_length=500,  # max length of generated summary
            min_length=100,  # min length of generated summary
            do_sample=False,
            truncation=True  # if file size is too large, truncate values
        )
        
        return summary[0]['summary_text']
    
    except ValueError as e:
        raise ValueError(f"Invalid input: {e}")
    
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred during summarization: {e}")
