from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination
import pandas as pd

# Create dataset
data = pd.DataFrame({
    'rain': ['no','no','yes','yes','no','yes','yes','no'],
    'trafficjam': ['yes','no','yes','no','yes','yes','no','no'],
    'arrivelate': ['yes','no','yes','no','no','yes','yes','no']
})

# Convert columns to categorical
for col in data.columns:
    data[col] = data[col].astype('category')

# Define model
model = DiscreteBayesianNetwork([
    ('rain', 'trafficjam'),
    ('trafficjam', 'arrivelate')
])

# Fit model
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Print CPDs
print(model.get_cpds())

# Inference
inference = VariableElimination(model)

query_result = inference.query(
    variables=['arrivelate'],
    evidence={'rain': 'yes'}
)

print(query_result)