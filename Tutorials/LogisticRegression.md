# LOGISTIC REGRESSION


### Classification
- **Classification:** *supervised machine learning that tries to predict which class or category some entity belongs to, based on its features, with some mathematical expression. E.g. analyzing company employees and trying to establish a dependence on some __feature__ or __variable___, like level of education, number of years in role, age, salary, &c.*
  - **Observation:** *the set of data related to one entity.*
  - **Variables:** *variables, of __features__, of the data.*
    - **Independent variables:** *inputs or predictors, these do not depend on other features. (E.g. level of education, age, time in current position.) Usually denoted with (x1, x2, ... xr).*
    - **Dependent variables:** *outputs or reponses, these depend on the independent variables. (E.g. salary, odds for promotion.) Usually denoted with (y0 or y1).*
  - **Regression problems:** *these have continuous and usually unbounded outputs (e.g. estimating the salary as a function of experience and education level).*
  - **Classification problems:** *tend to have discrete and finite outputs, called __classes__ or __categories__.*
    - **Binary/Binomial Classification:** *exactly two classes to choose from (0/1, True/False, positive/negative).*
    - **Multiclass/Multinomial Classification:** *three or more classes of the outputs to choose from.*

### Understanding When to Classify
- Examples of when to use classification:
  - *Text classification algorithms separate legitimate and spam emails*
  - *Sorting positive and negative comments*
  - *Credit scoring, applications, biological classification...*
  - *Image recognition tasks (human face or not? mouse or elephant?*
- **Logistic Regression:** *a fundamental classification technique, belongs to a group of __linear classifiers__. Fast and relatively uncomplicated. Essentially a method for binary classification (but can be applied to multiclass problems too).*
  - **Sigmoid Function**: *a mathematical function having an "S-shaped" curve. All sigmoids have the property that they map the entire number line into a small range between 0<>1 or -1<>1 (such that the use of a sigmoid function to convert a real value to a value that can be interpreted as a __probability__. The commonest sigmoid is the __Logistic Function__, which maps any real value from 0<>1 (which maps the variables (x1, x2... xr).*
  - **Natural Logarithm Function**: *```log(x)```-> as x approaches 0, the natural log of 'x' drops toward negative infinity. When ```x=1, log(x)=0```. The opposite is true for ```log(1-x)```.*
    - ```math.log(x)```, ```numpy.log(x)``` => natural logarithm of 'x' in Python (it is otherwise often denoted with 'ln' instead of 'log').



### Problem Formulation
- Logistic regression applied to binary classification: implementing logistic regression of some dependent variable ```y``` on the set of independent variables x=```(x₁, x₂, ..., xᵣ)``` where 'r' is the number of predictors/inputs.
  - **Goal:** *find the __logistic regression function__ ```p(x)``` such that the __predicted responses__ ```p(xᵢ)``` are as close as possible to the __actual response__ ```yᵢ``` for each observation ```i=1, ..., n```. (Each ```p(xᵢ)``` should be close to either 0 or 1– convenient!). Once you have the function ```p(x)```, you can use it to predict the outputs for new and unseen inputs (assuming the underlying mathematical dependence is unchanged).*

### Methodology
- **Logit:** ```f(x) = b₀ + b₁x₁ + ... + bᵣxᵣ```
  - **Estimators:** *the variables b0, b1,...,br, also called __prediction weights__ or just __coefficients__.*







