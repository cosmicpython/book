<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:h="http://www.w3.org/1999/xhtml"
                xmlns="http://www.w3.org/1999/xhtml"
                exclude-result-prefixes="h">

  <!-- Add title heading elements for different admonition types that do not already have headings in markup -->
  <xsl:param name="add.title.heading.for.admonitions" select="1"/>

  <!-- Override to print example captions without labels-->
  <xsl:template match="h:div[@data-type='example']/h:h5" mode="process-heading">
    <p><em>
      <xsl:apply-templates/>
    </em></p>
  </xsl:template>

    <!-- Drop @width attributes from table headers if present -->
  <xsl:template match="h:th/@width"/>
  
       <!-- OVERRIDE FOR ADDING HANDLING FOR EPILOGUE XREFS and FORMAL ELEMENTS-->
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
