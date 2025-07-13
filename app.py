import streamlit as st
import random
from streamlit_extras.let_it_rain import rain

# ------------------- Dynamic Level Generator -------------------
def generate_random_level(level_num):
    max_target = 30 + level_num * 25
    target = random.randint(10 + level_num * 5, max_target)

    base_coins = [1]
    possible_coins = [2, 3, 5, 7, 10, 15, 20, 25, 50]
    num_extra_coins = random.randint(2, 4)
    extra_coins = random.sample(possible_coins, num_extra_coins)
    coins = list(set(base_coins + extra_coins))
    coins.sort()

    return {"target": target, "coins": coins}

# ------------------- Algorithm -------------------
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    if dp[amount] == float('inf'):
        return None, []

    res = []
    while amount > 0:
        res.append(parent[amount])
        amount -= parent[amount]

    return dp[-1], res

# ------------------- Streamlit Config -------------------
st.set_page_config("💰 Optimum Coin Change Game", layout="centered")
st.title("🎮 Optimum Coin Change Game")
st.caption("Use the **least number of coins** to reach the target! 🧠💡")

# ------------------- Session State Init -------------------
if 'level' not in st.session_state:
    st.session_state.level = 0
    st.session_state.score = 0
    st.session_state.attempts = 0
    st.session_state.hint_used = False
    st.session_state.success = False
    st.session_state.level_data = generate_random_level(0)

level = st.session_state.level
target = st.session_state.level_data["target"]
coins = st.session_state.level_data["coins"]

# ------------------- Game End -------------------
if level >= 5:  # Set total number of random levels
    st.balloons()
    st.markdown("## 🎉 Game Completed!")
    st.success(f"🏆 Final Score: {st.session_state.score} points")
    st.button("🔁 Play Again", on_click=lambda: st.session_state.update(
        level=0, score=0, attempts=0, hint_used=False, success=False,
        level_data=generate_random_level(0)
    ))
    st.stop()

# ------------------- Level UI -------------------
st.markdown(f"### 🎯 Level {level + 1}")
st.markdown(f"**Target Amount:** {target}")
st.markdown(f"🪙 **Coins Available:** {', '.join(map(str, coins))}")

user_input = st.text_input("Enter coins used (comma separated)", placeholder="e.g. 10,10,5")

col1, col2 = st.columns([1, 1])
with col1:
    show_hint = st.button("💡 Show Hint")
with col2:
    submitted = st.button("✅ Submit")

# ------------------- Hint System -------------------
if show_hint:
    st.session_state.hint_used = True
    _, optimal_combination = coin_change(coins, target)
    if optimal_combination:
        st.info(f"🔍 Hint: Try using around **{len(optimal_combination)}** coins.")
    else:
        st.warning("⚠️ No solution with given coins.")

# ------------------- Submission Check -------------------
if submitted:
    st.session_state.attempts += 1
    try:
        user_coins = [int(x.strip()) for x in user_input.split(",") if x.strip()]
        if sum(user_coins) != target:
            st.error("❌ Your coin total doesn't match the target!")
        elif any(c not in coins for c in user_coins):
            st.warning("⚠️ You used coins not available in this level.")
        else:
            used = len(user_coins)
            optimal, opt_combo = coin_change(coins, target)
            if used == optimal:
                st.success(f"🎉 Perfect! You used the optimal number of coins: {used}")
                rain(emoji="🏅", font_size=40)
                bonus = 10 if not st.session_state.hint_used else 7
                st.session_state.score += bonus
                st.session_state.success = True
            else:
                st.info(f"✅ You used {used} coins. Optimal is {optimal}. Try again!")
                st.session_state.success = False
    except:
        st.error("Invalid input! Please enter numbers separated by commas.")

# ------------------- Navigation -------------------
if st.session_state.success:
    st.button("➡️ Next Level", on_click=lambda: st.session_state.update(
        level=st.session_state.level + 1,
        level_data=generate_random_level(st.session_state.level + 1),
        hint_used=False,
        success=False
    ))
else:
    st.button("🔁 Try Again")

# ------------------- Score & Attempts -------------------
st.markdown("---")
st.markdown(f"🏅 Score: **{st.session_state.score}**")
st.markdown(f"🎯 Attempts: {st.session_state.attempts}")
