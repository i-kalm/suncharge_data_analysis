import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

from sklearn.cluster import AgglomerativeClustering
from sklearn.manifold import TSNE

from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA as SKLearnPCA

import calendar



class Dataframes:
    def print_summary(self, dataframes, df_name):
        """
        Prints the shape, data types, and summary statistics of numerical columns
        for the specified DataFrame name if it exists in the provided dictionary.

        Parameters:
        - dataframes: Dictionary of DataFrames.
        - df_name: String, key name of the DataFrame in the dictionary.
        """
        if df_name in dataframes:
            df = dataframes[df_name]
            print(f"Shape of {df_name}: {df.shape}")
            print(f"Data Types in {df_name}:")
            print(df.dtypes)
            # Printing the number of unique values in each column
            print("\nNumber of Unique Values in Each Column:")
            for column in df.columns:
                print(f"{column}: {df[column].nunique()} unique values")
                
            print("\nSummary Statistics for Numerical Columns in", df_name)
            print(df.describe())        
            print("\nFirst 2 rows of", df_name)
            print(df.head(2))
        else:
            print(f"DataFrame named '{df_name}' not found in the provided dictionary.")
            
class Histograms:
    def plot_horizontal(self, ax, dataframe, column, title='Counts of Categories', title_fontsize=10, ylabel_tick_fontsize=8, xlabel_tick_fontsize=8, count_fontsize=8):
        """
        Plots a customized count plot for a specified column in a DataFrame on a given Axes object,
        with adjustable font sizes and adds count values on top of each bar with adjustable font size.

        Parameters:
        - ax: matplotlib Axes, the axes on which to draw the plot.
        - dataframe: pandas DataFrame containing the data.
        - column: str, name of the column to plot.
        - title: str, title of the plot.
        - title_fontsize: int, font size for the plot title.
        - xlabel_fontsize: int, font size for the x-axis label.
        - ylabel_tick_fontsize: int, font size for the y-axis tick labels.
        - xlabel_tick_fontsize: int, font size for the x-axis tick labels.
        - count_fontsize: int, font size for the count values annotated on the bars.
        """
        sns.countplot(ax=ax, data=dataframe, y=column, color='skyblue')
        ax.set_title(title, fontsize=title_fontsize)
        
        ax.set_xlabel('')
        ax.set_ylabel('')

        # Adjust font size of the tick labels
        ax.tick_params(axis='y', labelsize=ylabel_tick_fontsize)
        ax.tick_params(axis='x', labelsize=xlabel_tick_fontsize)

        # Adding count values on top of each bar with adjusted font size
        for p in ax.patches:
            ax.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2),
                        xytext=(5, 0), textcoords='offset points', va='center', ha='left', fontsize=count_fontsize)
                      
    
    
    def plot_vertical(self, data, column, figsize=(3, 2.5), fontsize=8, title="count of", title_fontsize=9):
        """
        Plots a vertical histogram of the specified column in the given DataFrame,
        with counts displayed on top of each bar as integers, no y-axis values, and adjusted y-axis limits.

        Parameters:
        - data: pandas.DataFrame containing the data.
        - column: str, the name of the column to plot.
        - figsize: tuple of int, the figure size. Default is (3, 2.5).
        - fontsize: int, the font size for titles and labels. Default is 8.
        - title: str, the title of the plot. Default is "count of".
        - title_fontsize: int, the font size for the plot title. Default is 9.
        """
        figsize = tuple(float(dim) for dim in figsize)
        
        plt.figure(figsize=figsize)
        ax = sns.countplot(data=data, x=column)
        plt.title(title, fontsize=title_fontsize)
        plt.ylabel('')
        plt.xlabel('')
        plt.tick_params(axis='x', labelsize=fontsize)
        plt.xticks(rotation=45)
        ax.set(yticklabels=[])
        ax.yaxis.set_major_formatter(plt.NullFormatter())

        # Calculate the maximum count to set y-axis limit dynamically
        max_count = data[column].value_counts().max()
        ax.set_ylim(0, max_count + max_count * 0.2)  # Add 20% more space above the highest bar

        # Adding the values on top of the bars as integers
        for p in ax.patches:
            ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', fontsize=fontsize, color='black', xytext=(0, 5),
                        textcoords='offset points')
        
        plt.show()
        
    def plot_monthly_quantity_distribution(self, data, date_column, quantity_column, figsize=(10, 2), fontsize=8, title="Monthly Quantity Distribution", axis_grid=True, grid_linestyle='--', grid_linewidth=0.5, value_format='{:.1f} K'):
        """
        Plots the monthly quantity distribution from a given DataFrame, grouping data by month.

        Parameters:
        - data: DataFrame containing the data to be plotted.
        - date_column: str, the name of the column in 'data' that contains date information.
        - quantity_column: str, the name of the column in 'data' that contains quantity values to be summed and plotted.
        - figsize: tuple of int, the figure size for the plot. Default is (10, 2).
        - fontsize: int, the font size for text and ticks on the plot. Default is 8.
        - title: str, the title of the plot. Default is "Monthly Quantity Distribution".
        - axis_grid: bool, whether to display the grid lines on the y-axis. Default is True.
        - grid_linestyle: str, the linestyle for the grid. Default is '--'.
        - grid_linewidth: float, the linewidth for the grid lines. Default is 0.5.
        - value_format: str, the format string for displaying values on top of the bars. Default is '{:.1f} K'.

        This function converts the 'date_column' to datetime, extracts the month, groups the data by month,
        sums the 'quantity_column' for each month, and plots the results as a bar chart. The values displayed
        on top of the bars are formatted according to 'value_format', which by default divides the values by 1000
        and appends 'K' (e.g., '1.5 K' for 1500). The function allows customization of the figure size, font size,
        plot title, grid appearance, and value formatting.
        """
        # Convert 'date_column' to datetime and extract the month
        data[date_column] = pd.to_datetime(data[date_column])
        data['month'] = data[date_column].dt.month
        
        # Group by month and sum the quantities
        monthly_data = data.groupby('month')[quantity_column].sum()

        # Start plotting
        fig, ax = plt.subplots(figsize=figsize)
        monthly_data.plot(kind='bar', ax=ax)

        # Add values on top of the bars using the specified format
        for index, value in enumerate(monthly_data):
            value_in_k = value_format.format(value/1000)  # Apply the format
            plt.text(index, value, value_in_k, ha='center', va='bottom', fontsize=fontsize)

        # Dynamically set the y-axis limit
        max_count = monthly_data.max()
        ax.set_ylim(0, max_count + max_count * 0.2)

        # Set the title and customize x-ticks
        plt.title(title, fontsize = fontsize+1)
        plt.xticks(ticks=range(0, 12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45, fontsize=fontsize)

        # Optionally remove y-axis values
        ax.set_yticklabels([])

        # Optionally add grid to the background
        if axis_grid:
            ax.set_axisbelow(True)  # Ensure grid is behind the bars
            ax.yaxis.grid(True, which='major', linestyle=grid_linestyle, linewidth=grid_linewidth)

        plt.show()

    def polar_plot(self, df1, df1_quantity_column, df2, df2_quantity_column, plot1_title="Gross Inventory", plot2_title="Inventory in Transit", legend_font_size=8, tick_params_fontsize=8, figsize=(10, 4)):
        """
        Plots polar charts for inventory quantities across months for different years.
        ...
        """
        # Adjusted part to calculate 'years' variable
        # Extract unique years from both df1 and df2
        unique_years_df1 = df1['Year'].unique()
        unique_years_df2 = df2['Year'].unique()
        
        # Find common years between df1 and df2
        common_years = np.intersect1d(unique_years_df1, unique_years_df2)
        
        # Sort the common years to ensure chronological order
        years = np.sort(common_years)

        # Aggregate data for df1
        df1_agg = df1.groupby(['Year', 'Month'])[df1_quantity_column].sum().unstack(0)
        
        # Aggregate data for df2
        df2_agg = df2.groupby(['Year', 'Month'])[df2_quantity_column].sum().unstack(0)
        
        # Setup the figure and subplots
        fig, axs = plt.subplots(1, 2, figsize=figsize, subplot_kw=dict(polar=True))
        
        # Common function to plot each subplot
        def plot_subplot(ax, data, title, years):
            num_vars = len(data.index)
            angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
            angles += angles[:1]  # Complete the loop
            
            for year in years:
                # Check if the year exists in this dataframe to avoid KeyError
                if year in data.columns:
                    values = data[year].values.flatten().tolist()
                    values += values[:1]  # Complete the loop for values
                    ax.plot(angles, values, linewidth=1, linestyle='solid', label=f'Year {year}')
                    ax.fill(angles, values, alpha=0.25)
            
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels([calendar.month_abbr[month] for month in range(1, 13)], fontsize=tick_params_fontsize)
            ax.tick_params(axis='y', labelsize=tick_params_fontsize)
            ax.set_title(title, fontsize=10, pad=20)
        
        # Plot for 'df1'
        plot_subplot(axs[0], df1_agg, plot1_title, years)
        
        # Plot for 'df2'
        plot_subplot(axs[1], df2_agg, plot2_title, years)
        
        # Adjust layout and add a common legend
        plt.tight_layout()
        fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=3, fontsize=legend_font_size)
        
        plt.show()


class Clusterer:
    def __init__(self):
        self.scaler = StandardScaler()
    
    def plot_hierarchical_clustering(self, data, figsize=(12, 4), max_d=5, dendrogram_p=5, sample_frac=0.1, title = 'Hierarchical Clustering Dendrogram'):
        """
        Performs hierarchical clustering on a sample of the provided DataFrame (excluding datetime columns)
        and plots a dendrogram.
        """
        # Sample the data if sample_frac is less than 1
        if sample_frac < 1.0:
            data = data.sample(frac=sample_frac)

        # Exclude datetime columns and proceed with the rest of the function as before
        df_numeric = data.select_dtypes(exclude=['datetime64[ns]'])
        df_encoded = pd.get_dummies(df_numeric)
        df_encoded.replace([np.inf, -np.inf], np.nan, inplace=True)
        df_encoded.fillna(df_encoded.mean(), inplace=True)
        
        scaler = StandardScaler()
        df_scaled = scaler.fit_transform(df_encoded)
        
        df_Z = linkage(df_scaled, method='ward')
        
        plt.figure(figsize=figsize)
        plt.title(title, fontsize=10)
        plt.xlabel('Data Points', fontsize=8)
        plt.ylabel('Distance', fontsize=8)
        dendrogram(df_Z, truncate_mode='level', p=dendrogram_p)
        plt.axhline(y=max_d, color='r', linestyle='--')
        plt.show()
        
    def visualize_clusters(self, data, n_clusters=4, metric='euclidean', linkage='ward', figsize=(6, 4), sample_frac=1.0, title = 'Cluster Visualization'):
        """
        Performs Agglomerative Clustering on a sample of the scaled data, assigns cluster labels,
        uses t-SNE for dimensionality reduction, and plots the clusters.

        Parameters:
        - data: DataFrame, the original data for adding cluster labels.
        - n_clusters: int, the number of clusters to form. Default is 4.
        - figsize: tuple, the figure size for the plot. Default is (6, 4).
        - sample_frac: float, the fraction of data to sample for clustering. Default is 1.0 (use all data).
        """
        
        # Sample the data if sample_frac is less than 1
        if sample_frac < 1.0:
            data = data.sample(frac=sample_frac)

        # Exclude datetime columns and one-hot encode the categorical data
        df_numeric = data.select_dtypes(exclude=['datetime64[ns]'])
        df_encoded = pd.get_dummies(df_numeric)
        
        # Handle NaN and infinite values
        df_encoded.replace([np.inf, -np.inf], np.nan, inplace=True)  # Convert inf to NaN
        df_encoded.fillna(df_encoded.mean(), inplace=True)  # Fill NaNs with the mean
        
        # Scale the data
        df_scaled = self.scaler.fit_transform(df_encoded)
        
        # Perform Agglomerative Clustering
        agglom = AgglomerativeClustering(n_clusters=n_clusters, metric=metric, linkage=linkage)
        agglom.fit(df_scaled)
        labels = agglom.labels_
        
        # Check the size of the dataset to set perplexity
        n_samples = len(df_scaled)
        perplexity_value = min(30, max(n_samples / 3, 1))  # Adjust perplexity based on the dataset size

        # Dimensionality reduction using t-SNE with adjusted perplexity
        tsne = TSNE(n_components=2, random_state=42, perplexity=perplexity_value)
        df_tsne = tsne.fit_transform(df_scaled)        
               
        # Plotting
        plt.figure(figsize=figsize)
        sns.scatterplot(x=df_tsne[:, 0], y=df_tsne[:, 1], hue=labels, palette="viridis", legend="full")
        plt.title(title)
        plt.xlabel("t-SNE Feature 1")
        plt.ylabel("t-SNE Feature 2")
        plt.legend(title='Cluster', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.show()
        
class CustomPCA:
    def perform_pca(self, data, n_components=4, categorical_cols=[], ignore_cols=[], plot_loadings=True, plot_title = 'PCA Component Loadings'):
        """
        Performs PCA on the given dataset after excluding specified columns, one-hot encoding specified 
        categorical columns, handling NaNs and infinite values, and scaling the features. It returns the 
        explained variance ratio and optionally plots a heatmap of component loadings.

        Parameters:
        - data: DataFrame, the input data.
        - n_components: int, the number of principal components to compute.
        - categorical_cols: list, column names to be treated as categorical and one-hot encoded.
        - ignore_cols: list, column names to be ignored in the analysis.
        - plot_loadings: bool, whether to plot the PCA component loadings heatmap. Default is True.

        Returns:
        - A message including the explained variance ratio and the total variance explained.
        - Optionally, a heatmap visualization of the PCA component loadings if plot_loadings is True.
        """
        # Exclude ignored columns
        df = data.drop(columns=ignore_cols, errors='ignore')
        
        # One-hot encode the specified categorical data
        if categorical_cols:
            encoded = pd.get_dummies(df, columns=[col for col in categorical_cols if col in df.columns])
        else:
            encoded = pd.get_dummies(df)
        
        encoded.replace([np.inf, -np.inf], np.nan, inplace=True)  # Convert inf to NaN
        encoded.fillna(encoded.mean(), inplace=True)  # Fill NaNs with the mean of each column

        # Scale the data
        scaled = StandardScaler().fit_transform(encoded)

        # Principal component analysis
        pca = SKLearnPCA(n_components=n_components)
        principalComponents = pca.fit_transform(scaled)
        principalDf = pd.DataFrame(data=principalComponents,
                                   columns=[f'Principal Component {i+1}' for i in range(n_components)])
        
        # Calculate the explained variance ratio and total variance explained
        explained_variance_ratio = pca.explained_variance_ratio_
        total_variance_explained = sum(explained_variance_ratio)
        print_message = (f"Explained variance ratio: {explained_variance_ratio}, "
                         f"Total variance explained by the first {n_components} components: "
                         f"{total_variance_explained:.2f} or {total_variance_explained * 100:.2f}%")

        # Optionally compute and plot PCA component loadings
        if plot_loadings:
            loadings = pca.components_
            feature_names = encoded.columns
            loadings_df = pd.DataFrame(loadings.T, columns=[f'PC{i+1}' for i in range(n_components)], index=feature_names)
            
            # Plotting the heatmap
            plt.figure(figsize=(10, 6))
            ax = sns.heatmap(loadings_df, cmap='viridis', annot=True, fmt=".2f", annot_kws={"size": 8})
            plt.title(plot_title)
            ax.set_ylabel('Features')
            ax.set_xlabel('Principal Components')
            plt.xticks(fontsize=8)
            plt.yticks(fontsize=8, rotation=0)
            plt.show()
        
        return print_message
        
class Correlations:
    def __init__(self):
        # Initialize the scaler
        self.scaler = StandardScaler()

    def plot_correlation_matrix(self, data, figsize=(12, 7), font_scale=0.75, cmap='coolwarm', vmin=-1, vmax=1,\
    linewidths=0.5, annot_kws={"size": 8}, categorical_cols=[], encode_categorical=True, ignore_cols=[], plot_title = 'Correlation Matrix Heatmap'):
        """
        Generates a heatmap for the correlation matrix of the given DataFrame, with options to exclude specific columns,
        and to one-hot encode specified categorical columns.

        Parameters:
        - data: DataFrame, the input data for which the correlation matrix will be computed.
        - figsize: tuple, the size of the figure (width, height) in inches.
        - font_scale: float, scaling factor for the font size of the plot.
        - cmap: str, the colormap for the heatmap.
        - vmin, vmax: float, values to anchor the colormap.
        - linewidths: float, width of the lines that will divide each cell.
        - annot_kws: dict, keyword arguments for `sns.heatmap` annotation.
        - categorical_cols: list, column names to be treated as categorical and one-hot encoded.
        - encode_categorical: bool, whether to one-hot encode specified categorical columns.
        - ignore_cols: list, column names to be ignored in the analysis.
        """
        # Set the context for the plot
        sns.set(context='notebook', style='white', font_scale=font_scale)

        df = data.copy()

        # Drop ignored columns
        df.drop(columns=ignore_cols, errors='ignore', inplace=True)

        # Ensure categorical treatment is correctly applied
        if encode_categorical and categorical_cols:
            # Filter out the categorical columns that actually exist in the DataFrame to avoid KeyErrors
            existing_categorical_cols = [col for col in categorical_cols if col in df.columns]
            df = pd.get_dummies(df, columns=existing_categorical_cols, drop_first=False)

        # No need to select only numeric columns after encoding, as all columns should be numeric now
        correlation_matrix = df.corr()

        # Create the heatmap
        plt.figure(figsize=figsize)
        sns.heatmap(correlation_matrix, 
                    annot=True, 
                    cmap=cmap, 
                    vmin=vmin, vmax=vmax, 
                    linewidths=linewidths, 
                    annot_kws=annot_kws)
        plt.title(plot_title)
        plt.show()
