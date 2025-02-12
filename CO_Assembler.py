import re

class Assembler():
    def __init__(self):
        self.register_encoding = {'zero':'00000','ra':'00001','sp':'00010','gp':'00011','tp':'00100','t0':'00101','t1':'00110','t2':'00111','s0':'01000','fp':'01000','s1':'01001','a0':'01010',
        'a1':'01011','a2': '01100', 'a3': '01101', 'a4': '01110', 'a5': '01111', 'a6': '10000', 'a7': '10001'
        ,'s2': '10010', 's3': '10011', 's4': '10100', 's5': '10101', 's6': '10110', 's7': '10111', 's8': '11000', 's9': '11001', 's10': '11010', 's11': '11011',
         't3': '11100','t4': '11101','t5': '11110','t6': '11111'}

        self.riscv_instructions = {"R-type": {
                                        "add": {"opcode": "0110011", "funct3": "000", "funct7": "0000000"},
                                        "sub": {"opcode": "0110011", "funct3": "000", "funct7": "0100000"},
                                        "and": {"opcode": "0110011", "funct3": "111", "funct7": "0000000"},
                                        "or": {"opcode": "0110011", "funct3": "110", "funct7": "0000000"},
                                        "slt": {"opcode": "0110011", "funct3": "010", "funct7": "0000000"},
                                        "srl": {"opcode": "0110011", "funct3": "101", "funct7": "0000000"}},
                                    "I-type": {
                                        "addi": {"opcode": "0010011", "funct3": "000"},
                                        "jalr": {"opcode": "1100111", "funct3": "000"},
                                        "lw": {"opcode": "0000011", "funct3": "010"}},
                                    "S-type": {
                                        "sw": {"opcode": "0100011", "funct3": "010"}},
                                    "B-type": {
                                        "beq": {"opcode": "1100011", "funct3": "000"},
                                        "bne": {"opcode": "1100011", "funct3": "001"}},
                                    "J-type": {
                                        "jal": {"opcode": "1101111"}}}

        self.data = None #will be updated during runtime
        self.ins_type_dict = dict()

    @classmethod
    def dec_bin(cls,num,length=0):
        '''returns a binary representation of the decimal number in string format (in unsigned representation)'''
        string = ''
        while num!=0:
            bit = num&1
            string += str(bit)
            num >>= 1
        if length != 0:
            string += '0'*(length-len(string))
        return string[::-1]

    @classmethod
    def read_file(cls,filename):
        with open(filename,'r') as f:
            data = list(map(lambda x:x.strip(),f.readlines()))
        return data

    def find_command(self,data):
        '''Takes the data from file and checks for command'''
        command = data.split()[0]
        for ins_type in self.riscv_instructions:
            if command in riscv_instructions[ins_type].keys():
                return command,ins_type
        else:
            raise Exception("Invalid Instructions")
    
    def update_dict(self):
        '''Maps each of the instruction types to their implementation in this class'''
        pass

    def Rtypeins(self,data):
        aux_data = re.split(r'[,\s]+',data)
        command,rd,rs1,rs2 = aux_data 
        other_info = self.riscv_instructions["R-type"][command] #funct7,funct3,opcode
        try:
            return f'{other_info['funct7']}{self.register_encoding[rs2]}{self.register_encoding[rs1]}{other_info['funct3']}{self.register_encoding[rd]}{other_info['opcode']}'
        except Exception as e:
            print("ERROR FOUND",e,"Invalid Register Name")

if __name__ == '__main__':
    assembler = Assembler()
    filename = 'input.asm'
    assembler.data = Assembler().read_file(filename)
    for i in data:
        command,ins_type = assembler.find_command(data)
