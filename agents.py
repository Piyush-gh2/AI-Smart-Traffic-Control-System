from src.loader import load_data
from src.predictor import predict_traffic
from src.optimizer import optimize_signal
from src.rl_agent import get_state

def run_system():
    df = load_data()
    
    prediction = predict_traffic(df)
    signal = optimize_signal(prediction)
    state = get_state(prediction)
    
    return df, prediction, signal, state