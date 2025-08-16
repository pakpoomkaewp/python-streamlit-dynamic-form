import streamlit as st
import numpy as np
import pandas as pd

st.title('🔬 Understanding Random Seed Behavior in Streamlit')

st.subheader('📊 The Real Story: Seed Gets Reset Every Time!')

# Add a counter to see how many times script runs
if 'run_count' not in st.session_state:
    st.session_state.run_count = 0
st.session_state.run_count += 1

st.write(f"🔄 **Script has run {st.session_state.run_count} times**")

# Show current random state info
st.write("🎲 **Current random generator info:**")
st.code(f"Random generator internal state (first 5 values): {np.random.get_state()[1][:5]}")

st.subheader('Part 1: "Random" data (before seed)')
st.write("This happens BEFORE we set seed(42):")
random_before_seed = np.random.randn(5)
st.write(f"Random numbers: {random_before_seed}")

st.subheader('Part 2: Setting seed(42)')
st.write("Now we set the seed...")
np.random.seed(42)
st.write("✅ Seed set to 42")

st.subheader('Part 3: "Consistent" data (after seed)')
st.write("This happens AFTER we set seed(42):")
random_after_seed = np.random.randn(5)
st.write(f"Random numbers: {random_after_seed}")

st.subheader('📈 Chart Demonstration')
st.write("Chart 1 (before seed - should be 'random'):")
np.random.seed()  # Reset to truly random
chart1_data = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.line_chart(chart1_data)

st.write("Chart 2 (after setting seed to 42):")
np.random.seed(42)
chart2_data = pd.DataFrame(np.random.randn(10, 2), columns=['A', 'B'])
st.line_chart(chart2_data)

# Interactive element to trigger reruns
slider_val = st.slider('Move this to rerun the script', 0, 100, 50)

st.subheader('🧠 What Actually Happens:')
st.write("""
**Every time you move the slider, this ENTIRE script runs from top to bottom:**

1. 🔄 Script starts fresh (new Python execution)
2. 🎲 Random generator starts in some state
3. 📊 Chart 1 uses whatever random state exists
4. 🎯 `np.random.seed(42)` RESETS the generator to a known state
5. 📊 Chart 2 uses the reset state (always same result)

**The seed doesn't "persist" - it gets set fresh every single rerun!**
""")

st.subheader('🔍 Proof: Let\'s trace the sequence')
st.write("Let's manually trace what happens in each rerun:")

# Demonstrate the sequence
st.write("**Sequence trace:**")
np.random.seed()  # Start fresh
st.write(f"1. After fresh start: {np.random.randn(3)}")
np.random.seed(42)  # Reset to 42
st.write(f"2. After seed(42): {np.random.randn(3)}")
np.random.seed(42)  # Reset to 42 again
st.write(f"3. After seed(42) again: {np.random.randn(3)}")
st.write("👆 Notice: Steps 2 and 3 are identical because we reset to the same seed!")
