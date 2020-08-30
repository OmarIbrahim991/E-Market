import React from "react"
import styled from "styled-components"

const ProductCard = styled.div`
    margin: 1em;
    padding: 0.25em;
    border: 1px solid black;
    width: 300px;
    height: 400px;
`

const ProductImage = styled.img`
    display: block;
    width: 100%;
    height: 70%;
    margin: 0;
`

const Product = ({ imgLink, imgTitle }) => {
    return (
        <ProductCard>
            <ProductImage src={imgLink} alt={imgTitle} />
            <h3 style={{width:"100%", textAlign: "center"}}>Product Title</h3>
            <p className="description" style={{width:"100%", textAlign: "center"}}>This is the product's description</p>
            <button style={{width:"100%"}}>Show Details</button>
        </ProductCard>
    )
}

export default Product
