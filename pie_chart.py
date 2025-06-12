#!/usr/bin/env python3
"""
Optimized Product Stock Visualization Tool
Generates pie charts from CSV data with minimal memory footprint and maximum performance.
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import sys
from typing import Tuple, Optional
import numpy as np

# Constants for configuration
CSV_FILE = 'product_stock.csv'
REQUIRED_COLUMNS = {'Product', 'Stock'}
COLORS = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', 
          '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9']
FIGURE_SIZE = (10, 8)
EXPLODE_THRESHOLD = 30
DPI = 300

class StockVisualizer:
    """Optimized stock visualization class with minimal memory usage."""
    
    __slots__ = ['df', 'csv_path']
    
    def __init__(self, csv_file: str = CSV_FILE):
        self.csv_path = Path(csv_file)
        self.df = None
    
    def load_data(self) -> bool:
        """Load and validate CSV data efficiently."""
        if not self.csv_path.exists():
            print(f"Error: {self.csv_path} not found!")
            return False
        
        try:
            # Read only required columns to save memory
            self.df = pd.read_csv(
                self.csv_path, 
                usecols=list(REQUIRED_COLUMNS),
                dtype={'Product': 'string', 'Stock': 'int32'}  # Optimize data types
            )
            
            # Validate columns
            if not REQUIRED_COLUMNS.issubset(self.df.columns):
                missing = REQUIRED_COLUMNS - set(self.df.columns)
                print(f"Error: Missing columns: {missing}")
                return False
            
            # Remove any rows with missing data
            self.df.dropna(inplace=True)
            
            if self.df.empty:
                print("Error: No valid data found!")
                return False
                
            return True
            
        except (pd.errors.EmptyDataError, pd.errors.ParserError, ValueError) as e:
            print(f"Error reading CSV: {e}")
            return False
    
    def _get_chart_data(self) -> Tuple[pd.Series, pd.Series]:
        """Extract chart data efficiently."""
        return self.df['Product'], self.df['Stock']
    
    def _calculate_explode(self, stock_values: pd.Series) -> np.ndarray:
        """Calculate explode values vectorized for performance."""
        return np.where(stock_values < EXPLODE_THRESHOLD, 0.05, 0)
    
    def _setup_plot_style(self) -> None:
        """Configure matplotlib for optimal performance."""
        plt.style.use('default')  # Use default style for speed
        plt.rcParams.update({
            'figure.figsize': FIGURE_SIZE,
            'font.size': 10,
            'axes.titlesize': 16,
            'axes.titleweight': 'bold'
        })
    
    def create_visualization(self) -> Optional[plt.Figure]:
        """Create optimized pie chart visualization."""
        if self.df is None:
            return None
        
        products, stock_values = self._get_chart_data()
        
        # Pre-calculate values
        explode_values = self._calculate_explode(stock_values)
        total_products = len(products)
        colors_cycle = COLORS * ((total_products // len(COLORS)) + 1)
        
        # Create figure with optimal settings
        self._setup_plot_style()
        fig, ax = plt.subplots(figsize=FIGURE_SIZE)
        
        # Create pie chart with optimized parameters
        wedges, texts, autotexts = ax.pie(
            stock_values,
            labels=products,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors_cycle[:total_products],
            explode=explode_values,
            shadow=True,
            textprops={'fontsize': 10, 'weight': 'bold'}
        )
        
        # Optimize text rendering
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        # Set title
        ax.set_title('Product Stock Distribution', fontsize=16, fontweight='bold', pad=20)
        
        # Add optimized legend
        legend_labels = [f'{prod}: {stock}' for prod, stock in zip(products, stock_values)]
        ax.legend(wedges, legend_labels, title="Stock Units", 
                 loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        
        plt.tight_layout()
        return fig
    
    def print_statistics(self) -> None:
        """Print optimized statistics using vectorized operations."""
        if self.df is None:
            return
        
        stock_values = self.df['Stock']
        products = self.df['Product']
        
        # Vectorized calculations
        total_stock = stock_values.sum()
        avg_stock = stock_values.mean()
        max_idx = stock_values.idxmax()
        min_idx = stock_values.idxmin()
        
        print(f"\n{'='*50}")
        print("STOCK ANALYSIS")
        print(f"{'='*50}")
        print(f"Total Stock: {total_stock:,} units")
        print(f"Products: {len(products)}")
        print(f"Average Stock: {avg_stock:.1f} units")
        print(f"Highest: {products.iloc[max_idx]} ({stock_values.iloc[max_idx]} units)")
        print(f"Lowest: {products.iloc[min_idx]} ({stock_values.iloc[min_idx]} units)")
    
    def save_chart(self, fig: plt.Figure, filename: str = 'stock_chart.png') -> bool:
        """Save chart with optimal settings."""
        try:
            fig.savefig(filename, dpi=DPI, bbox_inches='tight', 
                       facecolor='white', edgecolor='none')
            print(f"Chart saved: {filename}")
            return True
        except Exception as e:
            print(f"Save error: {e}")
            return False
    
    def cleanup(self) -> None:
        """Clean up resources."""
        plt.close('all')
        if self.df is not None:
            del self.df

def main() -> int:
    """Main execution function with error handling."""
    visualizer = StockVisualizer()
    
    try:
        # Load and validate data
        if not visualizer.load_data():
            return 1
        
        # Create visualization
        fig = visualizer.create_visualization()
        if fig is None:
            print("Failed to create visualization")
            return 1
        
        # Display statistics
        visualizer.print_statistics()
        
        # Show plot
        plt.show()
        
        # Optional save
        if input("\nSave chart? (y/N): ").lower() == 'y':
            visualizer.save_chart(fig)
        
        return 0
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        return 1
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 1
    finally:
        visualizer.cleanup()

if __name__ == "__main__":
    print("🔥 OPTIMIZED STOCK VISUALIZER")
    print("=" * 40)
    exit_code = main()
    sys.exit(exit_code)