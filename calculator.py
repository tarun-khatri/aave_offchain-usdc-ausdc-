class Calculator:
    def __init__(self, reserve_data):
        self.reserve_data = reserve_data
        self.liquidity_index = self.reserve_data[1]  
        self.ray = 1e27
        
        print(f"Debug - Raw Liquidity Index: {self.liquidity_index}")
        print(f"Debug - Normalized Liquidity Index: {self.liquidity_index / self.ray}")
    
    def calculate_usdc_from_ausdc(self, ausdc_amount):

        normalized_index = self.liquidity_index / self.ray
        usdc_amount = ausdc_amount * normalized_index
        
        print(f"Debug - aUSDC to USDC conversion:")
        print(f"Input aUSDC: {ausdc_amount}")
        print(f"Normalized Index: {normalized_index}")
        print(f"Calculated USDC: {usdc_amount}")
        
        return usdc_amount
    
    def calculate_ausdc_from_usdc(self, usdc_amount):

        ausdc_amount = usdc_amount
        
        print(f"Debug - USDC to aUSDC conversion:")
        print(f"Input USDC: {usdc_amount}")
        print(f"Calculated aUSDC: {ausdc_amount}")
        
        return ausdc_amount