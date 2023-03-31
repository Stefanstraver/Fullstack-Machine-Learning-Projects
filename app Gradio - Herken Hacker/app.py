import gradio as gr
import numpy as np
import joblib 

# predict functie
def predict(region1, region2, region3, region4, region5, region6):
    model = joblib.load('./localoutlierfactor.joblib')
    yhat = model.predict(np.array([[region1, region2, region3, region4, region5, region6]]))
    return 'Weird Traffic' if yhat == -1 else 'Normal Traffic'

# gradio interface
app = gr.Interface(
    title='Anomalieën in webverkeer ontdekken 🚦',
    fn=predict, 
    inputs=[gr.Slider(0,800),gr.Slider(0,800),gr.Slider(0,800),gr.Slider(0,800),gr.Slider(0,800),gr.Slider(0,800)], 
    outputs='text'
)

app.launch()