<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
		xmlns:xs="http://www.w3.org/2001/XMLSchema" exclude-result-prefixes="xs"
		xmlns:xd="http://www.oxygenxml.com/ns/doc/xsl" version="1.0"
		xmlns:protx="http://regis-web.systemsbiology.net/protXML">
  <!-- PRODUCES A TAB SEPARATED FILE FROM A PROT.XML FILE
       
       Takes one parameter to the define the protein prophet probability cutoff.

       Example: xsltproc -\-param p_threshold 0.5 <XSL_FILE> <XML_FILE>


       06-09-19: - Initial commit
       Patrick Pedrioli-->

  <xsl:output method="text" indent="no"/>
  <xsl:strip-space elements="*"/>

  <xsl:param name="p_threshold" select="1"/>

  
  <!-- Headers -->
  <xsl:template match="/">protein_id<xsl:text>
</xsl:text>
<xsl:apply-templates/>
  </xsl:template>

  <xsl:template match="protx:protein_group">
    <xsl:for-each select="protx:protein">
      <xsl:if test="@probability &gt;= $p_threshold">
	<xsl:value-of select="@protein_name"/>
	<xsl:text>
</xsl:text>
      </xsl:if>
    </xsl:for-each>
  </xsl:template>

</xsl:stylesheet>
