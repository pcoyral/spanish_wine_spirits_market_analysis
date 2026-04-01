"""
LVMH Competitive Analysis Module

This module provides utilities for analyzing LVMH's Wine & Spirits portfolio
positioning relative to the broader Spanish wine market.

Author: [Your Name]
Date: April 2026
Project: Spanish Wine & Spirits Market Analysis
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
import seaborn as sns


class LVMHAnalyzer:
    """
    Class for conducting LVMH competitive analysis in the Spanish W&S market.
    """
    
    # LVMH Wine & Spirits brands present in Spanish market
    LVMH_BRANDS = {
        'wine': [
            'Numanthia',  # Toro - Premium reds
            'Chandon',  # Sparkling wines (Cava)
            'Terrazas de los Andes',  # Argentine (competes in Spain)
            'Bodegas Chandon'
        ],
        'spirits': [
            'Hennessy',  # Cognac/Brandy
            'Belvedere',  # Vodka
            'Glenmorangie',  # Whisky
            'Ardbeg',  # Whisky
            'Château d\'Yquem'  # Sweet wine
        ]
    }
    
    # Premium segment price thresholds (EUR)
    PRICE_SEGMENTS = {
        'budget': (0, 5),
        'mass_market': (5, 10),
        'mid_premium': (10, 20),
        'premium': (20, 50),
        'luxury': (50, 100),
        'ultra_luxury': (100, float('inf'))
    }
    
    def __init__(self, market_data: pd.DataFrame, lvmh_data: Optional[pd.DataFrame] = None):
        """
        Initialize LVMH Analyzer
        
        Parameters:
        -----------
        market_data : pd.DataFrame
            Full Spanish wine market dataset
        lvmh_data : pd.DataFrame, optional
            Specific LVMH brand data (if separate)
        """
        self.market_data = market_data.copy()
        self.lvmh_data = lvmh_data.copy() if lvmh_data is not None else None
        self._identify_lvmh_products()
        
    def _identify_lvmh_products(self):
        """Identify LVMH products in the market dataset"""
        if 'winery' in self.market_data.columns or 'brand' in self.market_data.columns:
            brand_col = 'winery' if 'winery' in self.market_data.columns else 'brand'
            
            # Create LVMH flag
            all_lvmh_brands = self.LVMH_BRANDS['wine'] + self.LVMH_BRANDS['spirits']
            self.market_data['is_lvmh'] = self.market_data[brand_col].str.contains(
                '|'.join(all_lvmh_brands), 
                case=False, 
                na=False
            )
        else:
            self.market_data['is_lvmh'] = False
            
    def segment_by_price(self, price_column: str = 'price') -> pd.DataFrame:
        """
        Segment wines by price category
        
        Parameters:
        -----------
        price_column : str
            Name of the price column
            
        Returns:
        --------
        pd.DataFrame with added 'price_segment' column
        """
        def assign_segment(price):
            for segment, (min_p, max_p) in self.PRICE_SEGMENTS.items():
                if min_p <= price < max_p:
                    return segment
            return 'ultra_luxury'
        
        self.market_data['price_segment'] = self.market_data[price_column].apply(assign_segment)
        return self.market_data
    
    def calculate_market_share(self, 
                              segment: str = 'all',
                              by: str = 'volume') -> Dict[str, float]:
        """
        Calculate LVMH market share
        
        Parameters:
        -----------
        segment : str
            Price segment to analyze ('all', 'premium', 'luxury', etc.)
        by : str
            'volume' or 'value'
            
        Returns:
        --------
        Dict with LVMH and competitor shares
        """
        if segment != 'all':
            df = self.market_data[self.market_data['price_segment'] == segment]
        else:
            df = self.market_data
            
        if by == 'volume':
            lvmh_share = df['is_lvmh'].sum() / len(df) * 100
        else:  # value
            if 'price' in df.columns:
                lvmh_value = df[df['is_lvmh']]['price'].sum()
                total_value = df['price'].sum()
                lvmh_share = (lvmh_value / total_value) * 100
            else:
                lvmh_share = 0
                
        return {
            'lvmh_share': lvmh_share,
            'competitor_share': 100 - lvmh_share
        }
    
    def price_premium_analysis(self, price_column: str = 'price') -> pd.DataFrame:
        """
        Analyze LVMH price premium vs market
        
        Returns:
        --------
        DataFrame with price comparison statistics
        """
        results = []
        
        for segment in self.PRICE_SEGMENTS.keys():
            segment_data = self.market_data[
                self.market_data['price_segment'] == segment
            ]
            
            if len(segment_data) == 0:
                continue
                
            lvmh_prices = segment_data[segment_data['is_lvmh']][price_column]
            market_prices = segment_data[~segment_data['is_lvmh']][price_column]
            
            if len(lvmh_prices) > 0 and len(market_prices) > 0:
                premium = (lvmh_prices.mean() / market_prices.mean() - 1) * 100
                
                results.append({
                    'segment': segment,
                    'lvmh_avg_price': lvmh_prices.mean(),
                    'market_avg_price': market_prices.mean(),
                    'lvmh_median_price': lvmh_prices.median(),
                    'market_median_price': market_prices.median(),
                    'price_premium_pct': premium,
                    'lvmh_count': len(lvmh_prices),
                    'market_count': len(market_prices)
                })
        
        return pd.DataFrame(results)
    
    def distribution_channel_analysis(self, channel_col: str = 'channel') -> pd.DataFrame:
        """
        Compare LVMH vs market distribution strategies
        
        Parameters:
        -----------
        channel_col : str
            Column name for distribution channel
            
        Returns:
        --------
        DataFrame with channel distribution comparison
        """
        if channel_col not in self.market_data.columns:
            print(f"Warning: '{channel_col}' column not found")
            return pd.DataFrame()
        
        lvmh_dist = self.market_data[self.market_data['is_lvmh']][channel_col].value_counts(normalize=True) * 100
        market_dist = self.market_data[~self.market_data['is_lvmh']][channel_col].value_counts(normalize=True) * 100
        
        comparison = pd.DataFrame({
            'LVMH_%': lvmh_dist,
            'Market_%': market_dist,
            'Difference': lvmh_dist - market_dist
        }).fillna(0)
        
        return comparison
    
    def quality_rating_comparison(self, rating_col: str = 'rating') -> Dict:
        """
        Compare quality ratings between LVMH and market
        
        Parameters:
        -----------
        rating_col : str
            Column name for quality rating
            
        Returns:
        --------
        Dict with rating statistics
        """
        if rating_col not in self.market_data.columns:
            return {}
        
        lvmh_ratings = self.market_data[self.market_data['is_lvmh']][rating_col].dropna()
        market_ratings = self.market_data[~self.market_data['is_lvmh']][rating_col].dropna()
        
        return {
            'lvmh_mean': lvmh_ratings.mean(),
            'lvmh_median': lvmh_ratings.median(),
            'lvmh_std': lvmh_ratings.std(),
            'market_mean': market_ratings.mean(),
            'market_median': market_ratings.median(),
            'market_std': market_ratings.std(),
            'rating_advantage': lvmh_ratings.mean() - market_ratings.mean()
        }
    
    def geographic_presence(self, region_col: str = 'region') -> pd.DataFrame:
        """
        Analyze geographic presence: LVMH vs market
        
        Parameters:
        -----------
        region_col : str
            Column name for geographic region
            
        Returns:
        --------
        DataFrame with regional presence comparison
        """
        if region_col not in self.market_data.columns:
            return pd.DataFrame()
        
        lvmh_regions = self.market_data[self.market_data['is_lvmh']][region_col].value_counts()
        market_regions = self.market_data[~self.market_data['is_lvmh']][region_col].value_counts()
        
        comparison = pd.DataFrame({
            'LVMH_Count': lvmh_regions,
            'Market_Count': market_regions,
            'LVMH_Share_%': (lvmh_regions / (lvmh_regions + market_regions)) * 100
        }).fillna(0)
        
        return comparison.sort_values('LVMH_Share_%', ascending=False)
    
    def resilience_analysis(self, 
                           time_col: str = 'year',
                           value_col: str = 'price') -> pd.DataFrame:
        """
        Analyze market resilience during crisis periods (e.g., COVID-19)
        
        Parameters:
        -----------
        time_col : str
            Column name for time period
        value_col : str
            Column name for value metric
            
        Returns:
        --------
        DataFrame with time series comparison
        """
        if time_col not in self.market_data.columns:
            return pd.DataFrame()
        
        # Group by time period
        lvmh_trend = self.market_data[self.market_data['is_lvmh']].groupby(time_col)[value_col].agg(['mean', 'count'])
        market_trend = self.market_data[~self.market_data['is_lvmh']].groupby(time_col)[value_col].agg(['mean', 'count'])
        
        lvmh_trend.columns = ['LVMH_Avg', 'LVMH_Count']
        market_trend.columns = ['Market_Avg', 'Market_Count']
        
        comparison = pd.concat([lvmh_trend, market_trend], axis=1)
        comparison['LVMH_vs_Market_%'] = ((comparison['LVMH_Avg'] / comparison['Market_Avg']) - 1) * 100
        
        return comparison
    
    def plot_price_positioning(self, figsize: Tuple[int, int] = (12, 6)):
        """
        Visualize LVMH price positioning vs market
        """
        fig, axes = plt.subplots(1, 2, figsize=figsize)
        
        # Plot 1: Price distribution
        lvmh_prices = self.market_data[self.market_data['is_lvmh']]['price']
        market_prices = self.market_data[~self.market_data['is_lvmh']]['price']
        
        axes[0].hist([market_prices, lvmh_prices], 
                     bins=50, 
                     label=['Market', 'LVMH'],
                     alpha=0.7,
                     color=['#1f77b4', '#d62728'])
        axes[0].set_xlabel('Price (EUR)')
        axes[0].set_ylabel('Frequency')
        axes[0].set_title('Price Distribution: LVMH vs Market')
        axes[0].legend()
        axes[0].set_xlim(0, 100)  # Focus on 0-100 EUR range
        
        # Plot 2: Average price by segment
        premium_analysis = self.price_premium_analysis()
        if not premium_analysis.empty:
            x = range(len(premium_analysis))
            width = 0.35
            
            axes[1].bar([i - width/2 for i in x], 
                       premium_analysis['market_avg_price'],
                       width,
                       label='Market Avg',
                       color='#1f77b4')
            axes[1].bar([i + width/2 for i in x], 
                       premium_analysis['lvmh_avg_price'],
                       width,
                       label='LVMH Avg',
                       color='#d62728')
            axes[1].set_xlabel('Price Segment')
            axes[1].set_ylabel('Average Price (EUR)')
            axes[1].set_title('Average Price by Segment: LVMH vs Market')
            axes[1].set_xticks(x)
            axes[1].set_xticklabels(premium_analysis['segment'], rotation=45, ha='right')
            axes[1].legend()
        
        plt.tight_layout()
        return fig
    
    def generate_report(self) -> Dict:
        """
        Generate comprehensive LVMH competitive analysis report
        
        Returns:
        --------
        Dict with all key metrics and insights
        """
        report = {
            'overall_market_share': self.calculate_market_share('all', 'volume'),
            'premium_market_share': self.calculate_market_share('premium', 'value'),
            'luxury_market_share': self.calculate_market_share('luxury', 'value'),
            'price_premium': self.price_premium_analysis(),
            'quality_comparison': self.quality_rating_comparison(),
        }
        
        return report


def calculate_portfolio_metrics(lvmh_data: pd.DataFrame, 
                                market_data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate portfolio-level metrics for LVMH vs market
    
    Parameters:
    -----------
    lvmh_data : pd.DataFrame
        LVMH portfolio data
    market_data : pd.DataFrame
        Full market data
        
    Returns:
    --------
    DataFrame with portfolio metrics comparison
    """
    metrics = []
    
    # Portfolio concentration (HHI)
    def calculate_hhi(df, column):
        shares = df[column].value_counts(normalize=True)
        return (shares ** 2).sum() * 10000
    
    # Revenue volatility
    def calculate_cv(prices):
        return (prices.std() / prices.mean()) * 100
    
    metrics.append({
        'metric': 'Portfolio Concentration (HHI)',
        'LVMH': calculate_hhi(lvmh_data, 'region'),
        'Market': calculate_hhi(market_data, 'region')
    })
    
    metrics.append({
        'metric': 'Price Volatility (CV%)',
        'LVMH': calculate_cv(lvmh_data['price']),
        'Market': calculate_cv(market_data['price'])
    })
    
    return pd.DataFrame(metrics)


if __name__ == "__main__":
    print("LVMH Competitive Analysis Module")
    print("=" * 50)
    print("This module provides utilities for analyzing")
    print("LVMH's position in the Spanish W&S market.")
    print("\nUsage:")
    print("  from src.lvmh_analysis import LVMHAnalyzer")
    print("  analyzer = LVMHAnalyzer(market_data)")
    print("  report = analyzer.generate_report()")
