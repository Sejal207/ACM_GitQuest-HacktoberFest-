class BankAccount{ 
    int acc_number;
    String acc_name;
    int balance;
    int money_deposit;
    int money_withdraw;

    BankAccount(int num,String name,int bal){
        acc_number=num;
        acc_name=name;
        balance=bal;
        
    }
    int deposit(int mon_d){
        money_deposit=mon_d;
        balance=balance+money_deposit;
        return balance;
    };
    int withdraw(int mon_w){
        money_withdraw=mon_w;
        balance=balance-money_withdraw;
        return balance;
    };
    int check_balance(){
       return balance;
    };
    public static void main(String[] args) {
        BankAccount ba=new BankAccount(345, "ccc", 10000);
        int your_balance=ba.check_balance();
        System.out.println("The balance is "+your_balance);
        int depositry=ba.deposit(200);
        
        System.out.println("The updated balance is "+depositry);
        int withdrawal=ba.withdraw(3000);
        System.out.println("The updated balance is "+withdrawal);
        
    }




}

