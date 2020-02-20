class classa():
    def classaf1(self,p1):
        print(p1)

def write_to_kv(p1 = [1],p2 = [2]):
    data = np.array([['','Col1','Col2'],
                ['Row1',p1,p2]])
                
    df = pd.DataFrame(data=data[1:,1:],
                  index=data[1:,0],
                  columns=data[0,1:])
    
    client.write('kv','admin/write_to_kv',df,index_cols=['Col1'])
    
    
    

