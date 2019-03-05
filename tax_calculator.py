class TaxCalculation():
    'This class is used to calculate TAX'
    
    def EnterIncome(self):
        'This function is used to enter your total income'
        amount=float(input("Enter you total CTC: "))
        self.amount = amount
        basic = (40*amount)/100
        hra = (30*amount)/100
        con_allowance = (2*amount)/100
        med_allowance = (2*amount)/100
        stat_bonus = (1*amount)/100
        other_allowance = (25*amount)/100
        
        return print("\n Income: "+str(amount)+" \n Basic :"+str(basic)+" \n HRA: "+str(hra)+ "\n Conveyance Allowance : "+str(con_allowance)+ "\n Medical Allowance: "+str(med_allowance)+ "\n Statutory Bonus : "+str(stat_bonus)+ "\n Other Allowance : "+str(other_allowance))

    def EnterInvestmentAmount(self):
        'Here you enter all the investment'
        annual_prof_tax = 2400
        annual_prov_fund = 21600
        std_deduction = 40000
        
        eighty_c = float(input("Investment in PPF "))
        eighty_d = float(input("Investment in Medical Insaurance: "))
        eighty_e = float(input("Investment in Education Loan: "))
        eighty_tta = float(input("Investment in Savings Account: "))
        eighty_g = float(input("Investment in Donations: "))
        
        if(self.amount > 250000):
            
            if(eighty_c >150000):
                deduction = self.amount - 150000
            else:
                deduction = self.amount - eighty_c

            if(eighty_d > 25000):
                deduction = deduction - 25000
            else:
                deduction = deduction - eighty_d

            deduction = deduction - eighty_e

            if(eighty_tta>10000):
                deduction = deduction - 10000
            else:
                deduction = deduction - eighty_tta

            deduction = deduction - ((self.amount*10)/100)

            print('After reducing all the investments made: ',deduction)

            deduction = deduction - annual_prof_tax - annual_prov_fund - std_deduction
        
        else:
            deduction = self.amount

        self.deduction = deduction
        
        return print('\nAfter reducing all the investments made, professional tax, provident fund and standard deduction: ',deduction)
    
    def CalculateTax(self):
        'Here We Calculate Tax'
        print("The final taxable income is: ",self.deduction)
        
        if(self.deduction <= 250000):
            tax = 'No Tax to be paid'
        
        elif(self.deduction >250000 and self.deduction <=500000):
            tax = (5*self.deduction)/100
        
        elif(self.deduction > 500000 and self.deduction<=1000000):
            tax = (10*self.deduction)/100
            
        else:
            tax = (20*self.deduction)/100
        
        return print('The tax you have to pay on taxable income: '+str(self.deduction)+' is '+str(tax))
    
s = TaxCalculation()
s.EnterIncome()
s.EnterInvestmentAmount()
s.CalculateTax()