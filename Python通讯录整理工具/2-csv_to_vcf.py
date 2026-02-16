import m_VCF3

# 测试：Contacts.csv -> output.vcf
CSV_FILE = "Contacts.csv"
OUTPUT_VCF = "output.vcf"

if __name__ == '__main__':
    try:
        print(f"读取: {CSV_FILE}")
        vcards = m_VCF3.csv_to_vcards(CSV_FILE)
        print(f"写入: {OUTPUT_VCF}，共 {len(vcards)} 条")
        m_VCF3.vcards_to_vcf(vcards, OUTPUT_VCF)
        print(f"完成。已写入 {OUTPUT_VCF}")
    except Exception as e:
        print(f"报错: {e}")
        raise
