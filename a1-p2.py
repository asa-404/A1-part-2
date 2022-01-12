from dataprep.connector import Connector
import asyncio


async def main():
    dc = Connector('./tmdb')
    df = await dc.query('movies', api_key="578152be1392218f6d775ceb67b4e4f6")
    return df

df = asyncio.run(main())

print(df)
