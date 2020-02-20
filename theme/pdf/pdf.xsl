<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:h="http://www.w3.org/1999/xhtml"
                xmlns="http://www.w3.org/1999/xhtml"
                exclude-result-prefixes="h">

  <!-- Do add border div for figure images in animal series -->
  <xsl:param name="figure.border.div" select="1"/>

  <!-- This param is required for animal_theme_sass, but not the old animal_theme -->
  <!-- Generate separate footnote-call markers, so that we don't
       need to rely on AH counters to do footnote numbering -->
  <xsl:param name="process.footnote.callouts.only" select="1"/>


<xsl:template name="string-replace-all">
  <xsl:param name="text"/>
  <xsl:param name="replace"/>
  <xsl:param name="by"/>
  <xsl:choose>
    <xsl:when test="contains($text, $replace)">
      <xsl:value-of select="substring-before($text,$replace)"/>
      <xsl:value-of select="$by"/>
      <xsl:call-template name="string-replace-all">
        <xsl:with-param name="text" select="substring-after($text,$replace)"/>
        <xsl:with-param name="replace" select="$replace"/>
        <xsl:with-param name="by" select="$by"/>
      </xsl:call-template>
    </xsl:when>
    <xsl:otherwise>
      <xsl:value-of select="$text"/>
    </xsl:otherwise>
  </xsl:choose>
</xsl:template>

<xsl:template match="h:img/@src">
  <xsl:choose>
  <xsl:when test="contains(., 'callouts/')">
    <xsl:variable name="newtext">
      <xsl:call-template name="string-replace-all">
        <xsl:with-param name="text" select="."/>
        <xsl:with-param name="replace" select="'png'"/>
        <xsl:with-param name="by" select="'pdf'"/>
      </xsl:call-template>
    </xsl:variable>
     <xsl:attribute name="src">
        <xsl:value-of select="$newtext"/>
     </xsl:attribute>
  </xsl:when>
  <xsl:otherwise>
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
   </xsl:otherwise>
  </xsl:choose>
</xsl:template>

<!-- OVERRIDE FOR ADDING HANDLING FOR EPILOGUE XREFS-->
  <xsl:template match="h:table|h:figure|h:div[@data-type='example']" mode="label.formal.ancestor">
    <xsl:choose>
      <!-- For Preface and Introduction, custom label prefixes for formal ancestor
	   (don't use label.markup template here, as these labels are typically specific to just formal-object context -->
	   <!--BEGIN OVERRIDE -->
	     <xsl:when test="ancestor::h:section[@data-type = 'afterword']">E</xsl:when>
	     <!-- END OVERRIDE-->
	     
      <xsl:when test="ancestor::h:section[@data-type = 'preface']">P</xsl:when>
      <xsl:when test="ancestor::h:section[@data-type = 'introduction']">I</xsl:when>
      <xsl:otherwise>
	<!-- Otherwise, go ahead and use label.markup to get proper label numeral for ancestor -->
	<xsl:apply-templates select="(ancestor::h:section[contains(@data-type, 'acknowledgments') or
				     contains(@data-type, 'afterword') or
				     contains(@data-type, 'appendix') or
				     contains(@data-type, 'bibliography') or
				     contains(@data-type, 'chapter') or
				     contains(@data-type, 'colophon') or
				     contains(@data-type, 'conclusion') or
				     contains(@data-type, 'copyright-page') or
				     contains(@data-type, 'dedication') or
				     contains(@data-type, 'foreword') or
				     contains(@data-type, 'glossary') or
				     contains(@data-type, 'halftitlepage') or
				     contains(@data-type, 'index') or
				     contains(@data-type, 'introduction') or
				     contains(@data-type, 'preface') or
				     contains(@data-type, 'titlepage') or
				     contains(@data-type, 'toc')]|
				     ancestor::h:div[@data-type = 'part'])[last()]" mode="label.markup"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:template>

</xsl:stylesheet>
