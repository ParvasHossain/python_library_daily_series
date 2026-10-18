import asyncio
import httpx

# HTTPX Async Connection Pool with HTTP/2 support
async def fetch_urls():
    async with httpx.AsyncClient(http2=True) as client:
        # Reuses single socket and multiplexes requests
        responses = await asyncio.gather(
            client.get("https://httpbin.org/delay/1"),
            client.get("https://httpbin.org/delay/1")
        )
        return [r.status_code for r in responses]

# Executed concurrently via asyncio event loop
print(asyncio.run(fetch_urls()))