import joblib
class ModelPredictor:
  def __init__(self, model_path: str):
    self.model = joblib.load(model_path)
  def predict(self, text: str):
    prediction = self.model.predict([text])[0]
    probability = self.model.predict_proba([text])[0]
    return {"prediction": prediction, "probability": probability.tolist()}
