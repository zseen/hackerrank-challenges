public class TheCoinChangeProblem
{
    static HashMap hashMap = new HashMap();
    
    static long getWays(int totalMoney, long[] coins)
    {
    	return getWaysRecursive(totalMoney, coins, 0);
    }
    
    static long getWaysRecursive(int totalMoney, long[] coins, int index)
    {
        if (totalMoney == 0)
        {
            return 1;
        }

        if (index >= coins.length)
        {
            return 0;
        }

        String key = totalMoney + "-" + index;
        if (HashMap.isKeyInHashTable(key))
        {
            return HashMap.get(key);
        }
        
        long waysToPay = 0;
        
        int maxAmountToPayWithCoinType = 0;
        while (maxAmountToPayWithCoinType <= totalMoney)
        {
            int remainingMoney = totalMoney - maxAmountToPayWithCoinType;
            waysToPay += getWaysRecursive(remainingMoney, coins, index + 1);
            maxAmountToPayWithCoinType += coins[index];
            HashMap.add(key, (int) waysToPay);
        }

        return waysToPay;
    }

    public static void main(String[] args)
    {
    	int totalMoneyToPay = 15;
    	long[] coins = {49, 22, 45, 6, 11, 20, 30, 10, 46, 8, 32, 48, 2, 41, 43, 5, 39, 16, 28, 44, 14, 4, 27, 36};
        long ways = getWays(totalMoneyToPay, coins);
        System.out.println(ways);
    }
}
