<h1 align="center">🍿 Netflix Movie Recommender 🎥</h1>

<p align="center">
  <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGY0Y2hwZTczamxhNzg1dmExbnF2OXduZzRtZ2U0eGEzeTYzMHEybCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l3q2NESCqvcO2J1x6/giphy.gif" width="300" />
</p>

<p align="center">
  Recommend 🔍. Watch 🎬. Repeat 🔁.
</p>

<p align="center">
  Built with ❤️ using Python, Pandas, and Streamlit
</p>

---

## 🤖 What It Does

Imagine you just watched *Inception* and your brain is spinning 🌀…  
You want something **just as mind-blowing**.  
Boom 💥 — this app's got you.

- ✅ Takes your movie input  
- 🧠 Uses *cosine similarity* to find similar titles  
- 🎯 Recommends up to 10 movies  
- 🌐 Runs in your browser via Streamlit  

---

## 📦 Files You’ll Find

```
📁 netflix movie recommender/
├── 🧽 01_data_cleaning.ipynb — messy data, cleaned up
├── 🧠 02_model_building.ipynb — where the magic happens
├── 🖥️ streamlit_app.py — web app you can run
├── 📄 netflix_titles.csv — Netflix dataset
├── 🎓 imdb_top_1000.csv — IMDb Top 1000 for spice
├── 📜 README.md — you're reading it 😉
├── 📦 requirements.txt — install this stuff
```

---

## 🚀 Run It Locally Like a Pro

```bash
# Step 1: Clone this bad boy
git clone https://github.com/yourusername/netflix-recommender.git
cd netflix-recommender

# Step 2: Install dependencies
pip install -r requirements.txt

# Step 3: Launch the app
streamlit run streamlit_app.py
```

Then head to 👉 `http://localhost:8501`

---

## 🎯 How It Works (The Nerdy Bit)

- Every movie becomes a **vector of text features**
- We calculate how close (similar) each movie is to your input
- Closest matches = top recommendations 📼

---

## 🎬 Example Use

You type:  
> `"Inception"`

It replies with:  
- **Interstellar**  
- **Shutter Island**  
- **The Prestige**  
- **Tenet**  
(Yes, you're stuck in a Christopher Nolan loop 🌀)

---

## 💡 Future Madness

- 🤯 Add user-based recommendations (collaborative filtering)
- 🍅 Bring in Rotten Tomatoes or TMDB ratings
- 🐳 Docker support for "run anywhere" vibes
- 🧪 Add unit tests (because chaos needs structure too)

---

## 👨‍💻 About Me

**Abdul Muiz Munshi**  
🔗 GitHub: [@muiz2353673](https://github.com/muiz2353673)  
🔗 LinkedIn: [linkedin.com/in/abdul-muiz-munshi-6ab4141b8](https://linkedin.com/in/abdul-muiz-munshi-6ab4141b8)

---

<p align="center">
  Made with ❤️ and 🍿 in 2025  
  <br>
  <b>Last updated:</b> 14 July 2025
</p>
