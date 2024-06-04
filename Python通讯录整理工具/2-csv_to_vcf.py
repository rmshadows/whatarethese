import m_VCF3

# 要读取的CSV
CSV_FILE = "Contacts.csv"
# 输出的VCF
OUTPUT_VCF = "output.vcf"

if __name__ == '__main__':
    vcards = m_VCF3.csv_to_vcards(CSV_FILE)
    m_VCF3.vcards_to_vcf(vcards, OUTPUT_VCF)
