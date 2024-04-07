import ratelimit
import asyncio


async def call_func() -> None:
    print("Call func called")


async def main() -> None:
    session = 123  # Ensure args passed correctly
    for _ in range(200):
        await ratelimit_function(session)


@ratelimit.sleep_and_retry
@ratelimit.limits(calls=15, period=5)
@ratelimit.limits(calls=50, period=100, call_func_on_fail=call_func)
async def ratelimit_function(session):
    print(f"Making request... {session}")


if __name__ == "__main__":
    asyncio.run(main())