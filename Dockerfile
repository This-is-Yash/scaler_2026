FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install pydantic openai streamlit pandas
EXPOSE 7860
CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]