import m_VCF3

# 测试输入：250823.vcf
VCF_FILE = "1.vcf"
OUTPUT_CSV = "output.csv"

if __name__ == '__main__':
    try:
        print(f"读取: {VCF_FILE}")
        vcards = m_VCF3.readVCF(VCF_FILE)
        print(f"写入: {OUTPUT_CSV}")
        m_VCF3.vcards_to_csv(vcards, OUTPUT_CSV)
        print(f"完成。共 {len(vcards)} 条 -> {OUTPUT_CSV}")
    except Exception as e:
        print(f"报错: {e}")
        raise
