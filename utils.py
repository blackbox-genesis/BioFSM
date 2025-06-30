import matplotlib.pyplot as plt
import io

def plot_simulation(result):
    time = result[:, 0]
    gfp_col = [name for name in result.colnames if "GFP" in name][0]
    gfp = result[:, result.colnames.index(gfp_col)]

    plt.figure(figsize=(6, 3))
    plt.plot(time, gfp, label="GFP", color="green")
    plt.xlabel("Time")
    plt.ylabel("Concentration")
    plt.title("GFP Expression Over Time")
    plt.legend()

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches='tight')
    buf.seek(0)
    plt.close()
    return buf
