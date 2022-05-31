import './App.css';
import React from "react";


class ProductFilter extends React.Component {
    constructor(props) {
        super(props);
        this.handleFormInput = this.handleFormInput.bind(this);
        this.state = {
            series: 0,
            price: 0
        }
    }

    handleFormInput(series, price) {
        this.setState({
            series: series,
            price: price
        })
    }

    render() {
        const products = [
            {
                name: 'Механические часы Xiaomi CIGA Design Mechanical Watch ',
                price: 7800,
                series: 'Электроника',
                uri: "https://avatars.mds.yandex.net/get-marketpic/1690708/pic6a1392a16c7a6143c88fe021e16cd248/x248_trim"
            },
            {
                name: 'Босоножки женские/ Туфли летние открытые',
                price: 2800,
                series: 'Обувь',
                uri: "https://avatars.mds.yandex.net/get-mpic/5236741/img_id4840189718029065903.png/x248_trim"
            },
            {
                name: "Юбка-миди TOPTOP в винтажном стиле",
                price: 3493,
                series: 'Одежда',
                uri: "https://avatars.mds.yandex.net/get-mpic/5228682/img_id6227336725878168013.jpeg/x248_trim"
            },
            {
                name: "13.3 Ноутбук Apple MacBook Air 2020",
                price: 116000,
                series: 'Электроника',
                uri: "https://avatars.mds.yandex.net/get-marketpic/1599965/pic5d6e1453f3303f9657352ffb22d0230c/x248_trim"
            },
            {
                name: 'Материнская плата GIGABYTE B450 AORUS ELITE',
                price: 6240,
                series: 'Электроника',
                uri: "https://avatars.mds.yandex.net/get-mpic/4393885/img_id2682143401248561333.jpeg/x248_trim"
            },
            {
                name: 'Пуховик Sorelle Blossom Down мятный, XS',
                price: 23400,
                series: 'Одежда',
                uri: "https://avatars.mds.yandex.net/get-mpic/5346847/img_id191312590859555076.jpeg/x248_trim"
            },
            {
                name: 'Кроссовки New Balance Кроссовки мужские New Balance 608v1 MX608WT/D',
                price: 16990,
                series: 'Обувь',
                uri: "https://avatars.mds.yandex.net/get-mpic/5307434/img_id2002516434901135407.jpeg/x332_trim"
            }
        ];

        return (
            <div className="filter">
                <a style={{textAlign: "right", fontSize: 40}}>Я.Маркет</a>
                <MainFilterMenu
                    series={this.state.series}
                    price={this.state.price}
                    onFormInput={this.handleFormInput}
                />
                <ProductFilterResults
                    products={products}
                    series={this.state.series}
                    price={this.state.price}
                />
            </div>
        )
    }
}

//Меню с фильтрами
class MainFilterMenu extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange() {
        this.props.onFormInput(
            this.refs['seriesInput'].value,
            this.refs['priceInput'].checked
        );
    }

    render() {
        return (
            <form className="filter-menu">
                <label form="priceInput">Сортировка по цене</label>
                <input id="priceInput" type="checkbox" checked={this.props.price} ref="priceInput"
                       onChange={this.handleChange}/>
                <br/>
                <label form="seriesInput">Сортировка по категории:</label>
                <br/>
                <select id="seriesInput" ref="seriesInput" onChange={this.handleChange}>
                    <option value="All">Все категории</option>
                    <option value="Электроника">Электроника</option>
                    <option value="Одежда">Одежда</option>
                    <option value="Обувь">Обувь</option>
                </select>
            </form>
        );
    }
}

//Отфильтрованные результаты продуктов
class ProductFilterResults extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        const results = [];

        if (this.props.price === true) {
            this.props.products.sort((a, b) => {
                return b.price - a.price;
            })
        }

        this.props.products.map((product) => {
            if (this.props.series === 0 || this.props.series === 'All') {
                results.push(<Product product={product}/>);
            } else if (product.series === this.props.series) {
                results.push(<Product product={product}/>);
            }
        });

        return (
            <div className="filter-results">
                <ul className="blocks blocks_3up">
                    {results}
                </ul>
            </div>
        )
    }
}

//Класс продукта
class Product extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <li>
                <div className="feature">
                    <div className="feature-hd">
                        <h2 class="hdg hdg_2">{this.props.product.name}</h2>
                    </div>
                    <div className="feature-bd">
                        <p>{this.props.product.series}</p>
                    </div>
                    <div className="feature-image">
                        <img
                            src={this.props.product.uri}
                            alt="new"
                        />
                    </div>
                    <div className="feature-ft">
                        <p><b>{this.props.product.price} руб</b></p>
                    </div>
                </div>
            </li>
        )
    }
}

export default ProductFilter