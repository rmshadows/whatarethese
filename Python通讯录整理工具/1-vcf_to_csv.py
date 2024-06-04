import m_VCF3

# 要读取的VCF
VCF_FILE = "1.vcf"
# 输出的CSV
OUTPUT_CSV = "output.csv"

if __name__ == '__main__':
    vcards = m_VCF3.readVCF(VCF_FILE)
    m_VCF3.vcards_to_csv(vcards, OUTPUT_CSV)
