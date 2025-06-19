import math


class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        m = len(s)
        ans = set()

        def euler_sieve(n):
            # is_prime[i] 为 True 表示 i 是素数，False 表示 i 是合数
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False  # 0 和 1 不是素数

            primes = []  # 使用列表来存储素数，因为需要按顺序遍历
            # 后续转换成集合来加快查找速度

            for i in range(2, n + 1):
                # 如果 i 是素数，则加入素数列表
                if is_prime[i]:
                    primes.append(i)

                # 遍历已找到的素数列表 primes
                for p in primes:
                    # 如果当前数 i 乘以素数 p 超过了范围 n，则停止
                    # 因为 primes 是有序的，后面的素数会更大，乘积也会更大
                    if i * p > n:
                        break

                    # 标记 i * p 为合数
                    is_prime[i * p] = False

                    # 核心优化：确保每个合数只被其最小素因子筛掉一次
                    # 如果 i 能够被当前的素数 p 整除，
                    # 那么说明 p 是 i 的最小素因子。
                    # 此时，i * p 的最小素因子也是 p。
                    # 如果我们继续用 primes 中更大的素数去乘以 i，
                    # 比如 i * p' (p' > p)，那么 i * p' 的最小素因子仍然是 p (因为 p 是 i 的最小素因子)。
                    # 为了避免重复筛掉合数，并且保证每个合数只被其最小素因子筛掉，我们在此处中断内层循环。
                    # 例如：i=6, p=2。6%2==0。此时筛掉 12。
                    # 接下来不会用 p=3 来筛 6*3=18。18 会在 i=9, p=2 的时候被筛掉。
                    if i % p == 0:
                        break

            # 返回素数集合以便快速查找
            return set(primes)

        # 调用筛法，获取小于等于 int(s) 的所有素数
        max_val = int(s)
        nums = euler_sieve(max_val)

        # 再次强调：执行到这里，nums 集合中绝对不会包含 915，因为它是个合数。
        # print(f"DEBUG: nums (primes up to {max_val}): {nums}") # 调试输出

        # ----------------------------------------------------
        # 以下是你原始代码中处理字符串子串的逻辑，我将指出其中的问题
        # ----------------------------------------------------

        # 1. '2' in s 的逻辑问题：
        #   '2' in s 检查的是字符串 '2' 是否在字符串 s 中。
        #   例如 s = '915'，'2' 不在 '915' 中，所以这个 if 不会执行。
        #   即使 s = '123'，'2' 在 '123' 中，但你可能想检查的是数字 2，而不是字符串 '2'。
        #   如果子串是 '2'，会在后续的循环中被处理。
        #   所以这行代码通常是不必要且容易引起混淆的。
        # if '2' in s:
        #     ans.add(2) # 2 确实是素数，但这个判断条件不准确

        # 2. 遍历子串的逻辑问题：
        #   你原始代码中的 for j in range(i+1) 循环和 if num % 2 != 0 的判断有逻辑缺陷。
        #   它没有遍历所有可能的数字子串，并且对奇偶性的判断也是不必要的。
        #   所有可能的数字子串都应该被检查，无论其奇偶性。

        # 正确地遍历所有可能的数字子串，并检查它们是否为素数
        for i in range(m):
            for j in range(i, m):  # 从 i 到 m-1，遍历所有以 s[i] 开头的子串
                sub_str = s[i:j + 1]

                # 排除无效的数字子串，例如 "01" 这样的前导零（除非是 "0" 本身）
                if not sub_str or (len(sub_str) > 1 and sub_str[0] == '0'):
                    continue

                current_num = int(sub_str)

                # 只有当这个数字在筛法的范围内，并且在素数集合中，才添加到 ans
                # current_num <= max_val 这个条件通常隐含在 nums 的生成中，但明确写出来更安全
                if current_num <= max_val and current_num in nums:
                    ans.add(current_num)

        # print(f"DEBUG: ans set after checking substrings: {ans}") # 调试输出

        # 对 ans 中的素数进行排序并求和前三个
        q = sorted(list(ans), reverse=True)
        # print(f"DEBUG: Sorted primes (q): {q}") # 调试输出

        # 处理 q 长度不足 3 的情况
        if len(q) == 0:
            return 0
        elif len(q) < 3:
            return sum(q)
        else:
            return sum(q[:3])


# 创建 Solution 实例
S = Solution()

# 运行测试用例
# 请确保你的 Python 环境是干净的，没有缓存旧代码
result = S.sumOfLargestPrimes('915')
print(f"Result for '915': {result}")