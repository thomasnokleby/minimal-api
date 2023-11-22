if __name__ == "__main__":
    import uvicorn

    #    from dotenv import load_dotenv

    #    load_dotenv()

    uvicorn.run(
        "minimal_api.api:app", host="0.0.0.0", port=8000, log_level="debug", reload=True
    )
