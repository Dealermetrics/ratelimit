import ratelimit
import asyncio


class MySpecialClass:
    def __init__(self):
        self.threshold_hit = False

    async def call_func(self) -> None:
        print("Call func called")

    async def threshold_func(self) -> None:
        if not self.threshold_hit:
            print("Reached 80% of usage")
            self.threshold_hit = True


async def main() -> None:
    session = 123  # Ensure args passed correctly
    for _ in range(200):
        await ratelimit_function(session)

myclass = MySpecialClass()

@ratelimit.sleep_and_retry
@ratelimit.limits(calls=15, period=3)
@ratelimit.limits(calls=40, period=100, raise_on_limit=False, call_func_on_fail=myclass.threshold_func)
@ratelimit.limits(calls=50, period=100, call_func_on_fail=myclass.call_func)
async def ratelimit_function(session):
    print(f"Making request... {session}")


if __name__ == "__main__":
    asyncio.run(main())