# UINames API Python Wrapper

This is a light python wrapper for the [UINames API](https://uinames.com/) developed by [Thom](https://github.com/thm). It allows you to generate random identities (based on a few parameters) for use as mock user data.

### Installation

This library can be installed with pip:

```bash
pip install uinames
```

### Usage

#### *function* uinames.generate_random_identity()

This uses the UINames API to generate a single, random identity, and returns it in the form of a __Person__ class instance (explained below).

___

#### *function* uinames.generate_random_identities(amount=1, gender=None, region=None, minlen=None, maxlen=None, ext=False)

This uses the UINames API to generate 1 or more random identities, and returns it in the form of a __People__ class instance (explained below). Within the __People__ instance, the individual __Person__ instances can be accessed.

##### *Parameters*

All of the following parameters are optional, but have default values.

+ __amount__ - The number of identities to return. This should be an integer between `1` and `500` (inclusive). The default value for this parameter is `1`.
+ __gender__ - The desired gender of all the returned identities. This should be either ``"male"``, ``"female"``, or `None`. The default value for this parameter is `None`.
+ __region__ - The desired region of origin for all the returned identities. This can be one of the following: `"Albania"`, `"Argentina"`, `"Armenia"`, `"Australia"`, `"Austria"`, `"Azerbaijan"`, `"Bangladesh"`, `"Belgium"`, `"Bosnia and Herzegovina"`, `"Brazil"`, `"Canada"`, `"China"`, `"Colombia"`, `"Denmark"`, `"Egypt"`, `"England"`, `"Estonia"`, `"Finland"`, `"France"`, `"Georgia"`, `"Germany"`, `"Greece"`, `"Hungary"`, `"India"`, `"Iran"`, `"Israel"`, `"Italy"`, `"Japan"`, `"Korea"`, `"Mexico"`, `"Morocco"`, `"Netherlands"`, `"New Zealand"`, `"Nigeria"`, `"Norway"`, `"Pakistan"`, `"Poland"`, `"Portugal"`, `"Romania"`, `"Russia"`, `"Slovakia"`, `"Slovenia"`, `"Spain"`, `"Sweden"`, `"Switzerland"`, `"Turkey"`, `"Ukraine"`, `"United States"`, `"Vietnam"`, or `None`. The default value for this parameter is `None`.
+ __minlen__ - The desired minimum combined name and surname length. This should be an integer or `None`. The default value for this parameter is `None`.
+ __maxlen__ - The desired maximum combined name and surname length. This should be an integer or `None`. The default value for this parameter is `None`.
+ __ext__ - This should be a Boolean value. When set to `True`, this parameter causes all the returned entities to contain additional properties, such as: `age`, `title`, `phone`, `birthday`, `email`, `password`, `credit_card`, and `photo`. The default value for this parameter is `False`.

___

#### *class* uinames.models.People

A container for a collection of __Person__ class instances.

##### Attributes

+ __data__ - A list containing all of the __Person__ instances. This should be used to access the returned identities.

___

#### *class* uinames.models.Person

A container for a single identity and its properties.

##### Basic Attributes

+ __name__ - The first name of the returned identity.
+ __surname__ - The last name of the returned identity.
+ __gender__ - The gender of the returned identity. This will be either `"male"` or `"female"`.
+ __region__ - The region of origin of the identity. This will be one from the list above, in capitalized form.

##### Advanced Attributes

The following attributes will be present when the `ext` parameter is set to `True`.

+ __age__ - The age of the identity. This will an integer.
+ __title__ - The title of the identity. This will be either `"mr"` or `"mrs"`.
+ __phone__ - The phone number of the identity. This will be of the format `"(444) 444 4444"`.
+ __birthday__ - The birthday of the identity. This will be a dictionary containing the birthday in the following formats: `"DD/MM/YYYY"` (such as `"24/01/1985"`), `"MM/DD/YYYY"` (such as `"01/24/1985"`), and a raw integer value representing the time since Epoch (such as `475431301`).
+ __email__ - The email of the identity. This will be a string.
+ __password__ - The password of the identity. This will be a string.
+ __credit_card__ - The credit card information of the identity. This will contain the following data: An expiration field in the form `"MM/YY"` (such as `"3/19"`), the credit card number in the form `"XXXX-XXXX-XXXX-XXXX"` (such as `"2115-8343-4559-1249"`), the PIN number in the form `XXXX` (such as `2085`), and the security number in the form `XXX` (such as `143`).
+ __photo__ - An avatar of the identity. This will be a URL.

Note that accessing a non-existing property will raise a __PropertyUnavailable__ exception (uinames.utils.PropertyUnavailable).
