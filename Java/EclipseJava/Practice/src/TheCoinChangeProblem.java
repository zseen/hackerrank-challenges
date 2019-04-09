
public class TheCoinChangeProblem 
{
	static long getWays(int money, long[] coins, int index)
	{
		if (money == 0)
		{
			return 1;
		}
		
		if (index >= coins.length)
		{
			return 0;
		}
		
		int amountWithCoin = 0;
		long ways = 0;
		while (amountWithCoin <= money)
		{
			int remainingMoney = money - amountWithCoin;
			ways += getWays(remainingMoney, coins, index + 1);
			amountWithCoin += coins[index];
			
		}
		
		return ways;
    }

	public static void main(String[] args) 
	{	long[] coins = {2, 5, 3, 6};
		long ways = getWays(10, coins, 0);
		System.out.println(ways);

	}

}
