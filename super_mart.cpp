#include<iostream>
#include<fstream>
#include<windows.h>
using namespace std;

class Mart
{
    string Name; int Quantity, Price;
    public:
    Mart(){
        Name = "";
        Quantity=0;
        Price=0;
    }

    void setName(string Name){
        this->Name=Name;
    }

    void setQuantity(int Quantity){
        this->Quantity=Quantity;
    }

    void setPrice(int Price){
        this->Price=Price;
    }

    string getName(){
        return Name;
    }

    int getQuantity(){
        return Quantity;
    }

    int getPrice(){
        return Price;
    }};

void addItem(Mart m){
    string name; int quantity, price;
    cout<<"Kindly enter the Name of the product - ";
    cin>>name;
    m.setName(name);
    cout<<"Kindly enter the quantity of the product - ";
    cin>>quantity;
    m.setQuantity(quantity);
    cout<<"Kindly enter the price of the product - ";
    cin>>price;
    m.setPrice(price);

    ofstream out("C:/Users/Shreya/CODING/VS/Project/SuperMart.txt", ios:: app);
    if(!out){
        cout<<"Error! File cannot open";
    }
    else{
        out<<m.getName()<<" | "<<m.getQuantity()<<" | "<<m.getPrice()<<" | "<<endl;
        cout<<"Item save successfully"<<endl;
    }
    out.close();
}

void search(Mart m){
    string name;
    cout<<"Enter name of product - ";
    cin>>name;

    ifstream in("C:/Users/Shreya/CODING/VS/Project/SuperMart.txt");
    if(!in){
        cout<<"File not found";
    }
    else{
        string line;
        bool found= false;
        while(getline(in,line)){
            int pos= line.find(name);
            if(pos != string::npos){
                cout<<"Item | Quantity | Price\n";
                cout<<line<<endl;
                found=true;
            }
        }

        if (!found){
            cout<<"Product not found!"<<endl;
        }
    }
}


int main()
{
    Mart m;
    bool exit=false;
    while(!exit){
        system("cls");
    

    cout<<"Welcome to the Super Mart"<<endl;
    cout<<"*********************************************************************************************\n";
    cout<<"Kindly enter the corresponding number for the task which you would like to perform\n";
    cout<<"1. Add Items\n";
    cout<<"2. Search Items\n";
    cout<<"3. Exit\n";
    cout<<"Enter the number: ";

    int n;
    cin>>n;

    if (n==1)
    {
        system("cls");
        addItem(m);
        Sleep(5000);
    }
    else if(n==2){
        system("cls");
        search(m);
        Sleep(5000);
    }
    else if(n==3){
        exit=true;
        cout<<"Thank you!";
        Sleep(3000);
    }

}}

