# My Data Diary: 4 Months of My Life Under a Microscope

A personal data science project where I tracked 12+ daily variables for 4 months to understand what drives my productivity.

## 🎯 Research Question
Can I predict how focused I'll be tomorrow based on today's activities?  
What should I actually do differently?

## 📊 Data Collected (120 days)
- Sleep hours & quality
- Exercise minutes
- Screen time hours
- Focused study hours
- Social hours
- Nutrition score
- Caffeine intake
- Stress level
- Day of week
- Academic cycle

## 🔬 Methods Used
1. **Statistical testing** (t-tests, correlation, ANOVA)
2. **Machine learning** (Linear Regression, Random Forest, Gradient Boosting, Neural Network)
3. **Time-series cross-validation**
4. **Feature importance analysis**

## 📈 Key Findings
- Sleep quality and quantity significantly affect next-day productivity
- Exercise has a sweet spot (~45 minutes)
- Screen time negatively correlates with productivity
- Wednesdays are consistently more productive
- Best ML model: Random Forest (R² ≈ 0.65)

## 🚀 How to Run
```bash
pip install -r requirements.txt
python analysis.py
```
