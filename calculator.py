class MiningProfitabilityCalculator:
    def __init__(self, mining_hardware, electricity_cost, mining_difficulty, pool_fee):
        self.mining_hardware = mining_hardware
        self.electricity_cost = electricity_cost
        self.mining_difficulty = mining_difficulty
        self.pool_fee = pool_fee

    def calculate_profitability(self):
        total_profitability = 0

        for hardware in self.mining_hardware:
            hardware_name = hardware['name']
            hash_rate = hardware['hash_rate']
            power_consumption = hardware['power_consumption']
            hardware_cost = hardware['cost']

            # Calculate profitability metrics:
            mining_reward = self.calculate_mining_reward(hash_rate)
            electricity_cost = self.calculate_electricity_cost(power_consumption)
            pool_fee = self.calculate_pool_fee(mining_reward)
            profit = mining_reward - electricity_cost - pool_fee
            roi = hardware_cost / profit if profit > 0 else None

            # Print profitability metrics:
            print("Mining Hardware:", hardware_name)
            print("Mining Reward:", mining_reward)
            print("Electricity Cost:", electricity_cost)
            print("Pool Fee:", pool_fee)
            print("Profit:", profit)
            print("ROI:", roi)
            print("-----------------")

            total_profitability += profit

        # Print total profitability:
        print("Total Profitability:", total_profitability)

    def calculate_mining_reward(self, hash_rate):
        # Calculate mining reward based on mining difficulty
        mining_reward = hash_rate * self.mining_difficulty
        return mining_reward

    def calculate_electricity_cost(self, power_consumption):
        # Calculate electricity cost based on power consumption and electricity cost per unit
        electricity_cost = power_consumption * self.electricity_cost
        return electricity_cost

    def calculate_pool_fee(self, mining_reward):
        # Calculate pool fee based on mining reward and pool fee percentage
        pool_fee = mining_reward * self.pool_fee
        return pool_fee


# Example usage:
mining_hardware = [
    {
        'name': 'ASIC Miner A',
        'hash_rate': 1000,  # Hash rate in hashes per second
        'power_consumption': 100,  # Power consumption in watts
        'cost': 2000  # Hardware cost in USD
    },
    {
        'name': 'ASIC Miner B',
        'hash_rate': 2000,
        'power_consumption': 150,
        'cost': 3000
    }
]

electricity_cost = 0.12  # Electricity cost per unit in USD
mining_difficulty = 2000  # Mining difficulty
pool_fee = 0.02  # Pool fee as a decimal value

calculator = MiningProfitabilityCalculator(mining_hardware, electricity_cost, mining_difficulty, pool_fee)
calculator.calculate_profitability()
