import pandas as pd
import matplotlib.pyplot as plt

def broken_df(path: str, sep=None):
    """Read a CSV trying common non-UTF8 encodings."""
    for enc in ("utf-8", "utf-8-sig", "cp1252", "latin1", "iso-8859-1"):
        try:
            return pd.read_csv(path, encoding=enc, sep=sep)
        except UnicodeDecodeError:
            continue
    # last resort: ignore undecodable bytes
    return pd.read_csv(path, encoding="cp1252", sep=sep, encoding_errors="replace")

def plot_berri1(df, columns, x_col="Date"):
   
    df.plot(x=x_col, y=columns)
    plt.xlabel("Date")
    plt.ylabel("No. of Cyclists")
    plt.title("Selected Columns Plot of No. Of Cyclists On a Track Over Time")
    plt.legend()    

    return plt
 

def complaints_df(path:str, dtype="unicode"):
    """Read the complaints CSV with all columns as strings."""
    return pd.read_csv(path, dtype=dtype) 

import matplotlib.pyplot as plt



def plot_top_complaints(df, n):
    """
    Plot a bar chart of the top N most common complaint types.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe containing at least a 'Complaint Type' column.
    n : int
        Number of top complaints to plot.
    """

    # Compute top n complaint types
    top_n = df["Complaint Type"].value_counts().head(n)

    # Plot
    top_n.plot(kind="bar")

    plt.style.use("ggplot")
    plt.rcParams["figure.figsize"] = (12, 6)
    plt.title(f"Top {n} Most Common Complaint Types")
    plt.xlabel("Complaint Type")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    return plt

def complaint_by_borough(df, complaint_type):
    """
    Return the number of specific complaint type per borough.

    Parameters
    ----------
    df : pd.DataFrame
        The full complaints dataset.
    complaint_type : str
        The specific complaint type to filter on (default: Noise - Street/Sidewalk)

    Returns
    -------
    pd.Series
        Counts of specific complaints per borough (sorted descending)
    """

    # Filter
    is_complaint = df["Complaint Type"] == complaint_type #creates a dummy variable = true if the complaint type matches the one we want
    specific_complaints = df[is_complaint] #filters the dataframe to only include rows where is_complaint = true 
    
    
    counts = specific_complaints["Borough"].value_counts()
    counts.plot(kind="bar")
    plt.title(f"Number of '{complaint_type}' Complaints by Borough")
    plt.xlabel("Borough")
    plt.ylabel("Number of Complaints")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Count per borough
    return specific_complaints["Borough"].value_counts() #counting the filtered dataframe by borough to see which borough has the most complaints of that type
    